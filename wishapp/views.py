from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render_to_response


def desire (request):
    b = 'This is view'
    #accounts = Wishmakers.objects.all()
    # usermame = request.POST.get('username', '')
    # password = request.POST.get('password', '')
    return render_to_response('test.html', {'a': b})



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
