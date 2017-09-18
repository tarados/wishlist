from django.shortcuts import render
from wishapp.models import Wishmakers
import datetime

def desire (request):
    a = Wishmakers.objects.all()
# new user registration
    name = request.POST.get('name', 'guest')
    password = request.POST.get('passw', 'guest')
    if Wishmakers.objects.filter(user=name, password=password) != 'guest':
        account = Wishmakers.objects.filter(user=name, password=password)
    else:
        record = Wishmakers(user=name, password=password, publication_date=datetime.datetime.now())
        record.save()
# the creation of new desires
    if account:
        description = request.POST.get('desire', None)
        record = Wishmakers(user=name, password=password, description=description, publication_date=datetime.datetime.now())
        record.save()

    return render(request, 'test.html', locals())