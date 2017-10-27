from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from wishapp.models import Desire
from wishapp.forms import DesireForm
from django.contrib import auth
from wishapp.linkcoder import linkOn
import datetime
import re

def dreamers (request):
    arg = {}
    arg['username'] = auth.get_user(request).username
    arg['user_id'] = auth.get_user(request).id
    return render_to_response('dreamers.html', arg)

def dreamer (request, dreamer_id):
    desire_form = DesireForm
    arg = {}
    arg.update(csrf(request))
    arg['dreamer'] = User.objects.get(id=dreamer_id)
    arg['desires'] = Desire.objects.filter(desire_user_id=dreamer_id)
    result = []
    for l in arg['desires']:
        obj = {'id': l.id, 'text': linkOn(l.desire_text), 'text2': l.desire_text,
               'date': l.desire_date, 'desire_state': l.desire_state, 'order_user_id': l.desire_order_user_id}
        result.append(obj)
    arg['desire2'] = result
    arg['form'] = desire_form
    arg['username'] = auth.get_user(request).username
    arg['user_id'] = auth.get_user(request).id
    arg['date_now'] = datetime.datetime.now()
    return render_to_response('dreamer.html', arg)

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
    print(request.POST)
    print(obj.desire_state)
    return redirect('/dreamers/%s' % dreamer_id)

@csrf_exempt
def login1(request):
    arg = {}
    arg['dreamer_id'] = request.GET.get('dreamer_id')
    arg.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/dreamers/%d/' % int(request.POST.get('dreamer_id')))
        else:
            return redirect('/auth/register1/')
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
