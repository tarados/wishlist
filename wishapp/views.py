from django.shortcuts import render
from wishapp.models import Wishmaker
import datetime

def desire (request):
    login = request.POST.get('name', '')
    passw = request.POST.get('password', '')

    if Wishmaker.objects.filter(user=login, password=passw):
        account = Wishmaker.objects.filter(user=login)
    else:
        record = Wishmaker.objects.create(user=login, password=passw, description='', publication_date=datetime.datetime.now())
        record.save()
    a = Wishmaker.objects.all()
    return render(request, 'test.html', locals())