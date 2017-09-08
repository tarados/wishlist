from django.shortcuts import render
from wishapp import models
from wishapp.models import User, Wishmaker
import datetime

def desire (request):
    name = request.POST.get('name', '')
    desires = request.POST.get('desire', '')
    publication_date = datetime.datetime.now()
    a = name + ' ' + desires
    return render(request, 'index.html', locals())