from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.template.context_processors import csrf

def login(request):
    arg = {}
    arg.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            arg['login_error'] = 'User do not found'
            return render_to_response('login.html', arg)
    else:
        return render_to_response('login.html', arg)

def logout(request):
    auth.logout(request)
    return redirect('/')
