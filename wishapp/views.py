from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from wishapp.models import Desire, Desirelist
from wishapp.forms import DesireForm, DesireListForm
from django.contrib import auth
from wishapp.linkcoder import link_on
from wishapp.parse_img import get_img, find_url, get_url
import datetime
import json


# первая страница
def dreamers(request):
    dreamers = User.objects.all()
    user = auth.get_user(request)
    is_loggedin = user.id is None
    return render_to_response('dreamers.html', locals())

def desirelist(request, dreamer_id):
    is_ownerlist = True
    desirelists = Desirelist.objects.filter(desirelist_user_id=dreamer_id)
    list_count = desirelists.count
    user = auth.get_user(request)
    return render_to_response('desirelist.html', locals())


@csrf_exempt
def adddesirelist(request, dreamer_id):
    is_ownerlist = True
    desirelists = Desirelist.objects.filter(desirelist_user_id=dreamer_id)
    list_count = desirelists.count
    user = auth.get_user(request)
    form = DesireListForm(request.POST)
    if form.is_valid():
        desirelist = form.save(commit=False)
        desirelist.desirelist_user_id = dreamer_id
        form.save()
    else:
        return redirect('/desirelist/%d/' % int(dreamer_id))
    return render_to_response('desirelist.html', locals())


# страница добавлений, редактирования, архивирования и удаления желаний пользователя
def dreamer(request, dreamer_id, desirelist_id):
    arg = {}
    arg.update(csrf(request))
    dreamer = User.objects.get(id=dreamer_id)
    desires = Desire.objects.filter(desire_user_id=dreamer_id, desire_desirelist_id=desirelist_id).order_by('desire_order')
    desirelist = Desirelist.objects.get(id=desirelist_id)
    result = []
    height = 0
    for desire in desires:
        try:
            k = desire.determine_height_img()
            height = 150 * k
        except:
            pass
        if desire.desire_state != 2:
            if desire.desire_order_user is not None:
                order_user_name = desire.desire_order_user.username
            else:
                order_user_name = ''
            obj = {
                'id': desire.id,
                'text': link_on(desire.desire_text)[0],
                'link': link_on(desire.desire_text)[1],
                'title': desire.desire_title,
                'text_for_edit': desire.desire_text,
                'date': desire.desire_date,
                'desire_state': desire.desire_state,
                'desire_image': desire.desire_img,
                'desire_photo': desire.desire_photo,
                'order_user_name': order_user_name,
                'heigth_img': height
            }
            result.append(obj)
        else:
            pass
    desire_list = result
    form = DesireForm
    user = auth.get_user(request)
    username = user.username
    user_id = user.id
    arg['date_now'] = datetime.datetime.now()
    is_owner = user_id == int(dreamer_id)
    is_loggedin = user_id is None
    is_choice = user_id != int(dreamer_id)
    return render_to_response('dreamer.html', locals())


# модуль добавления желаний
@csrf_exempt
def adddesire(request, dreamer_id, desirelist_id):
    print(request.POST)
    # desire_id = request.POST.get('desire_id')
    if request.method == 'GET':
        form = DesireForm()
    if request.method == 'POST':
        form = DesireForm(request.POST)
        if form.is_valid():
            desire = form.save(commit=False)
            linkcoder = link_on(desire.desire_text)
            if linkcoder[2] != '#':
                desire.desire_img = linkcoder[2]
            elif linkcoder[1] != '#':
                desire.desire_img = get_img(linkcoder[1])
            desire.desire_user = User.objects.get(id=dreamer_id)
            desire.desire_date = datetime.datetime.now()
            desire.desire_desirelist_id = desirelist_id
            form.save()
            try:
                desire.fetch_remote_img(desire.desire_img)
            except:
                pass
            return redirect('/dreamers/%s/%s' % (dreamer_id, desirelist_id))
        else:
            return redirect('/dreamers/%s/%s' % (dreamer_id, desirelist_id))
    return redirect('/dreamers/%s/%s' % (dreamer_id, desirelist_id))


# модуль удаления желаний
@csrf_exempt
def deldesire(request, dreamer_id):
    if request.POST:
        desire_id = request.POST['deldesire']
        derise = Desire.objects.get(id=desire_id)
        derise.delete()
    return redirect('/dreamers/%s' % dreamer_id)


# модуль редактирования желаний
@csrf_exempt
def editdesire(request):
    dreamer_id = request.POST.get('dreamer_id')
    desire_id = request.POST.get('desire_id')
    desirelist_id = request.POST.get('desirelist_id')
    desire = Desire.objects.get(id=desire_id)
    if request.method == 'POST':
        form = DesireForm(request.POST, instance=desire)
        if form.is_valid():
            desire = form.save(commit=False)
            linkcoder = link_on(desire.desire_text)
            if linkcoder[2] != '#':
                desire.desire_img = linkcoder[2]
            elif linkcoder[1] != '#':
                desire.desire_img = get_img(linkcoder[1])
            desire.desire_user = User.objects.get(id=dreamer_id)
            desire.desire_date = datetime.datetime.now()
            form.save()
            try:
                desire.fetch_remote_img(desire.desire_img)
            except:
                pass
            return redirect('/dreamers/%s/%s/' % (dreamer_id, desirelist_id))
        else:
            return redirect('/dreamers/%s/%s/' %(dreamer_id, desirelist_id))
    return render_to_response('edit.html', locals())


# модуль выбора желаний для покупки
@csrf_exempt
def selectdesire(request):
    desire_id = request.POST.get('desire_id', '')
    dreamer_id = request.POST.get('dreamer_id', '')
    desire_order_user_id = request.POST.get('order_user_id', '')
    obj = Desire.objects.get(id=desire_id)
    obj.desire_state = 1
    obj.desire_order_user_id = desire_order_user_id
    obj.save()
    return redirect('/dreamers/%s' % dreamer_id)


# модуль архивирования желаний
@csrf_exempt
def backupdesire(request):
    print(request.POST)
    desire_id = request.POST.get('backupdesire', '')
    dreamer_id = request.POST.get('dreamer_id', '')
    obj = Desire.objects.get(id=desire_id)
    obj.desire_state = 2
    obj.save()
    print(obj)
    return redirect('/dreamers/%s' % dreamer_id)


# страница архива
@csrf_exempt
def archive(request, user_id):
    arg = {}
    desires = Desire.objects.filter(desire_user_id=user_id).order_by('desire_order')
    result = []
    for desire in desires:
        if desire.desire_state == 2:
            if desire.desire_order_user_id is not None:
                order_id = desire.desire_order_user_id
                order_username = desire.desire_order_user.username
            else:
                order_id = None
                order_username = ''
            obj = {
                'id': desire.id,
                'text': link_on(desire.desire_text)[0],
                'title': desire.desire_title,
                'text_for_edit': desire.desire_text,
                'image': desire.desire_img,
                'date': desire.desire_date,
                'desire_state': desire.desire_state,
                'order_user_id': desire.desire_order_user_id,
                'order_user_name': order_username
            }
            result.append(obj)
        else:
            pass
    desire_list = result
    user = auth.get_user(request)
    username = user.username
    user_id = user.id
    dreamer_id = user_id
    is_owner = True
    if username:
        return render_to_response('archive.html', locals())
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')



# модуль удаления желаний из архива
@csrf_exempt
def delarchive(request, user_id):
    if request.POST:
        desire_id = request.POST['deldesire']
        derise = Desire.objects.get(id=desire_id)
        derise.delete()
    return redirect('/dreamers/archive/%s' % user_id)


@csrf_exempt
def returnfromarchive(request, user_id):
    if request.POST:
        desire_id = request.POST.get('returndesire', '')
        desire = Desire.objects.get(id=desire_id)
        desire.desire_state = 0
        desire.save()
    return redirect('/dreamers/archive/%s' % user_id)


# модуль удаления желаний из sortlist
@csrf_exempt
def del_sort_desire(request, user_id):
    if request.POST:
        desire_id = request.POST['deldesire']
        derise = Desire.objects.get(id=desire_id)
        derise.delete()
    return redirect('/dreamers/sort/%s' % user_id)


@csrf_exempt
def order(request):
    odereded_list = request.POST.get("a")
    order_for_save = json.loads(odereded_list)
    for data in order_for_save:
        obj = Desire.objects.get(id=data['desire_id'])
        obj.desire_order = int(data['loopcounter'])
        obj.save()
    return HttpResponse('')


def sort(request, user_id):
    arg = {}
    desires = Desire.objects.filter(desire_user_id=user_id).order_by('desire_order')
    result = []
    for desire in desires:
        obj = {
            'id': desire.id,
            'title': desire.desire_title,
            'text': link_on(desire.desire_text)[0],
            'text_for_edit': desire.desire_text,
            'image': desire.desire_img,
            'date': desire.desire_date,
            'desire_state': desire.desire_state,
        }
        result.append(obj)
    desire_list = result
    user = auth.get_user(request)
    username = user.username
    user_id = user.id
    dreamer_id = user_id
    is_owner = True
    if username:
        return render_to_response('sort.html', locals())
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')
