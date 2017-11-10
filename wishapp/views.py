from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from wishapp.models import Desire
from wishapp.forms import DesireForm
from django.contrib import auth
from wishapp.linkcoder import link_on
import datetime


def dreamers(request):
    user = auth.get_user(request)
    username = user.username
    user_id = user.id
    return render_to_response('dreamers.html', locals())


def dreamer(request, dreamer_id):
    desire_form = DesireForm
    arg = {}
    arg.update(csrf(request))
    dreamer = User.objects.get(id=dreamer_id)
    desires = Desire.objects.filter(desire_user_id=dreamer_id)
    result = []
    for desire in desires:
        if desire.desire_state != 2:
            if desire.desire_order_user is not None:
                order_user_name = desire.desire_order_user.username
            else:
                order_user_name = ''
            obj = {
                'id': desire.id,
                'text': link_on(desire.desire_text),
                'text2': desire.desire_text,
                'date': desire.desire_date,
                'desire_state': desire.desire_state,
                'order_user_name': order_user_name
            }
            result.append(obj)
        else:
            pass
    desire2 = result
    form = desire_form
    user = auth.get_user(request)
    username = user.username
    user_id = user.id
    arg['date_now'] = datetime.datetime.now()
    is_owner = user_id == int(dreamer_id)
    is_loggedin = user_id is None
    is_choice = user_id != int(dreamer_id)
    print(is_owner)
    print(is_loggedin)
    print(is_choice)
    print(arg)
    return render_to_response('dreamer.html', locals())


@csrf_exempt
def adddesire(request, dreamer_id):
    if request.method == 'GET':
        form = DesireForm(instance=desire)
    if request.method == 'POST':
        form = DesireForm(request.POST)
        if form.is_valid():
            desire = form.save(commit=False)
            desire.desire_user = User.objects.get(id=dreamer_id)
            desire.desire_date = datetime.datetime.now()
            form.save()
    return redirect('/dreamers/%s' % dreamer_id)


@csrf_exempt
def deldesire(request, dreamer_id):
    if request.POST:
        desire_id = request.POST['deldesire']
        derise = Desire.objects.get(id=desire_id)
        derise.delete()
    return redirect('/dreamers/%s' % dreamer_id)


@csrf_exempt
def editdesire(request, dreamer_id, desire_id):
    desire = Desire.objects.get(id=desire_id)
    if request.method == 'GET':
        form = DesireForm(instance=desire)
    elif request.method == 'POST':
        form = DesireForm(request.POST, instance=desire)
        if form.is_valid():
            desire = form.save(commit=False)
            form.save()
            return redirect('/dreamers/%s' % dreamer_id)
    return render_to_response('edit.html', locals())


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


@csrf_exempt
def backupdesire(request):
    desire_id = request.POST.get('backupdesire', '')
    dreamer_id = request.POST.get('dreamer_id', '')
    obj = Desire.objects.get(id=desire_id)
    obj.desire_state = 2
    obj.save()
    return redirect('/dreamers/%s' % dreamer_id)


@csrf_exempt
def login1(request):
    arg = {}
    arg['dreamer_id'] = request.GET.get('dreamer_id')
    arg.update(csrf(request))
    print(arg)
    print(request.POST)
    print(request.GET)
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/dreamers/%d/' % int(request.POST.get('dreamer_id')))
        else:
            print(arg)
            print(request.POST)
            print(request.GET)
            dreamer_id = request.POST.get('dreamer_id')
            return redirect('/login1/?dreamer_id=%s' % dreamer_id)
    else:
        return render_to_response('login1.html', arg)


@csrf_exempt
def register1(request):
    arg = {}
    arg.update(csrf(request))
    arg['form'] = UserCreationForm
    arg['dreamer_id'] = request.POST.get('dreamer_id')
    if request.POST:
        new_user_form = UserCreationForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            newuser = auth.authenticate(username=new_user_form.cleaned_data['username'], password=new_user_form.cleaned_data['password2'])
            auth.login(request, newuser)
            dreamer_id = request.POST.get('dreamer_id', 1)
            return redirect('/dreamers/%d/' % int(dreamer_id))
        else:
            arg['form'] = new_user_form
    return render_to_response('register1.html', arg)


@csrf_exempt
def archive(request, user_id):
    arg = {}
    desires = Desire.objects.filter(desire_user_id=user_id)
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
                'text': link_on(desire.desire_text),
                'text2': desire.desire_text,
                'date': desire.desire_date,
                'desire_state': desire.desire_state,
                'order_user_id': desire.desire_order_user_id,
                'order_user_name': order_username
            }
            result.append(obj)
        else:
            pass
    desire2 = result
    user = auth.get_user(request)
    username = user.username
    user_id = user.id
    return render_to_response('archive.html', locals())


@csrf_exempt
def delarchive(request, user_id):
    if request.POST:
        desire_id = request.POST['deldesire']
        derise = Desire.objects.get(id=desire_id)
        derise.delete()
    return redirect('/dreamers/archive/%s' % user_id)