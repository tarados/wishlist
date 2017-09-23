from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf
from wishapp.models import Dreamer, Desire
from wishapp.forms import DesireForm


def dreamers (request):
   return render_to_response('dreamers.html', {'dreamers': Dreamer.objects.all()})

def dreamer (request, dreamer_id):
    desire_form = DesireForm
    arg = {}
    arg.update(csrf(request))
    arg['dreamer'] = Dreamer.objects.get(id=dreamer_id)
    arg['desires'] = Desire.objects.filter(desire_dreamer_id=dreamer_id)
    arg['form'] = desire_form
    return render_to_response('dreamer.html',arg)

def adddesire(request, dreamer_id):
    if request.POST:
        form = DesireForm(request.POST)
        if form.is_valid():
            desire = form.save(commit=False)
            desire.desire_dreamer = Dreamer.objects.get(id=dreamer_id)
            form.save()
    return redirect('/dreamers/%s' % dreamer_id)

