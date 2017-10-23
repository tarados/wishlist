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
        obj = {'id': l.id, 'text': linkOn(l.desire_text), 'text2': l.desire_text, 'date': l.desire_date}
        result.append(obj)
    arg['desire2'] = result
    arg['form'] = desire_form
    arg['username'] = auth.get_user(request).username
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
def selectdesire(request, dreamer_id, desire_id):
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
def login1(request):
    arg = {}
    arg.update(csrf(request))
    #print(request.POST)
    print(request.GET['currentdreamer'])
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            #arg['user_id'] = request.GET['currentdreamer']
            #arg['user_id'] = auth.get_user(request).id
            return redirect('/dreamers/%d/' % request.GET['currentdreamer'])
        else:
            return redirect('/auth/register/')
    else:
        return render_to_response('login.html', arg)