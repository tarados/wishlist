from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from wishapp.models import Dreamer, Desire


def dreamers (request):
   return render_to_response('dreamers.html', {'dreamers': Dreamer.objects.all()})

def dreamer (request, dreamer_id):
    return render_to_response('dreamer.html', {'dreamer': Dreamer.objects.get(id=dreamer_id), 'desires': Desire.objects.filter(desire_dreamer_id=dreamer_id)})


