from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf
from wishapp.models import Desire
from wishapp.forms import DesireForm

def dreamers (request):
   return render_to_response('dreamers.html', {'dreamers': User.objects.all()})

def dreamer (request, user_id):
    desire_form = DesireForm
    arg = {}
    arg.update(csrf(request))
    arg['dreamer'] = User.objects.get(id=user_id)
    arg['desires'] = Desire.objects.filter(desire_user_id=user_id)
    arg['form'] = desire_form
    return render_to_response('dreamer.html',arg)

def adddesire(request, user_id):
    if request.POST:
        form = DesireForm(request.POST)
        if form.is_valid():
            desire = form.save(commit=False)
            desire.desire_dreamer = User.objects.get(id=user_id)
            form.save()
    return redirect('/dreamers/%s' % user_id)

