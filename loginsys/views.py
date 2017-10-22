from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf


def login(request):
    arg = {}
    arg.update(csrf(request))
    print(request.POST)
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            arg['user_id'] = auth.get_user(request).id
            return redirect('/dreamers/%d/' % arg['user_id'])
        else:
            return redirect('/auth/register/')
    else:
        return render_to_response('login.html', arg)

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    arg = {}
    arg.update(csrf(request))
    arg['form'] = UserCreationForm
    if request.POST:
        new_user_form = UserCreationForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            newuser = auth.authenticate(username=new_user_form.cleaned_data['username'], password=new_user_form.cleaned_data['password2'])
            auth.login(request, newuser)
            arg['user_id'] = auth.get_user(request).id
            return redirect('/dreamers/%d/' % arg['user_id'])
        else:
            arg['form'] = new_user_form
    return render_to_response('register.html', arg)


