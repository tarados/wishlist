from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf
from wishapp.models import Desire
from wishapp.forms import DesireForm
from django.contrib import auth
import datetime

def dreamers (request):
    arg = {}
    arg['dreamers'] = User.objects.all()
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
    return render_to_response('dreamer.html',arg)

def adddesire(request, dreamer_id):
    if request.POST:
        form = DesireForm(request.POST)
        if form.is_valid():
            desire = form.save(commit=False)
            desire.desire_user = User.objects.get(id=dreamer_id)
            desire.desire_date = datetime.datetime.now()
            form.save()
    return redirect('/dreamers/%s' % dreamer_id)

def deldesire(request, dreamer_id):
    if request.POST:
        desire_id = request.POST['deldesire']
        derise = Desire.objects.get(id=desire_id)
        derise.delete()
        #derise.save()
    return redirect('/dreamers/%s' % dreamer_id)