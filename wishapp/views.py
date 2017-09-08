from django.shortcuts import render
import datetime

def desire (request):
    name = request.POST.get('name', '')
    desires = request.POST.get('desire', '')
    publication_date = datetime.datetime.now()
    a = name + ' ' + desires
    return render(request, 'index.html', locals())