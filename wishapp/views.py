import django as django
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render


def desire (request):
    #accounts = Wishmakers.objects.all()
    usermame = request.POST.get('username', '')
    password = request.POST.get('password', '')
    return render(request, 'test.html', locals())



# def login1(request):
#     username = request.POST.get('username', '')
#     password = request.POST.get('password', '')
#     user = auth.authenticate(username=username, password=password)
#
#
#     return render(request, 'test.html', locals())
#     # else:
#     #     # Отображение страницы с ошибкой
#     #     return HttpResponseRedirect('index.html')
#
#
# def logout(request):
#     auth.logout(request)
#     # Перенаправление на страницу.
#     return HttpResponseRedirect('/account/loggedout/')
