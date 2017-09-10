from django.shortcuts import render
from wishapp.models import Wishmaker
import datetime

def desire (request):
    name = request.POST.get('name', '')
    desires = request.POST.get('desire', '')
    if name:
        record = Wishmaker.objects.create(user=name, description=desires, publication_date=datetime.datetime.now())
        record.save()
    a = Wishmaker.objects.all()
    return render(request, 'index.html', locals())