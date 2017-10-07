from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from sqlalchemy import update

from wishapp.models import Desire
from wishapp.forms import DesireForm
from django.contrib import auth
from django.shortcuts import render, get_object_or_404
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
    arg['form'] = desire_form
    arg['username'] = auth.get_user(request).username
    if auth.get_user(request).id == int(dreamer_id):
        return render_to_response('dreamer.html', arg)
    else:
        return redirect('/auth/logout/')

@csrf_exempt
def adddesire(request, dreamer_id):
    print(request.POST)
    if request.POST:
        form = DesireForm(request.POST)
        if form.is_valid():
            desire = form.save(commit=False)
            if re.search(r'[h-s]\w+:[//.a-z:\d\w+]+', desire.desire_text):
                for c in re.findall(r'[h-s]\w+:[//.a-z:\d\w+]+', desire.desire_text):
                    desire.desire_text = desire.desire_text.replace(c, '<a href="' + c + '">' + c + '</a>')
                desire.desire_user = User.objects.get(id=dreamer_id)
                desire.desire_date = datetime.datetime.now()
            else:
                desire.desire_user = User.objects.get(id=dreamer_id)
                desire.desire_date = datetime.datetime.now()
            form.save()
    return redirect('/dreamers/%s' % dreamer_id)

def deldesire(request, dreamer_id):
    if request.POST:
        print(request.POST)
        desire_id = request.POST['deldesire']
        derise = Desire.objects.get(id=desire_id)
        derise.delete()
    return redirect('/dreamers/%s' % dreamer_id)

@csrf_exempt
def editdesire(request, dreamer_id, desire_id):
    print(request.POST)
    desire = Desire.objects.get(id=desire_id)
    if request.POST:
        form = DesireForm(instance=desire)
        if form.is_valid():
            desire = form.save(commit=False)
            form.save()
        return render_to_response('edit.html', locals())
    return redirect('/dreamers/%s' % dreamer_id)

