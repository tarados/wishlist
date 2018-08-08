from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from wishapp.forms import SignUpForm, Desirelist
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    arg = {}
    master_id = request.GET.get('dreamer_id', '')
    sub_id = request.GET.get('sub_id', '')
    arg.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        master_id = request.POST.get('master_id', '')
        sub_id = request.POST.get('sub_id', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            arg['user_id'] = auth.get_user(request).id
            if master_id != '':
                return redirect('/dreamers/%s/%s' % (master_id, sub_id))
            else:
                return redirect('/desirelist/%s' % arg['user_id'])
        else:
            password_error = '1'
            return render_to_response('dreamers.html', locals())
    else:
        return render_to_response('dreamers.html', locals())


def login_vk(request):
    arg = {}
    arg['user_id'] = auth.get_user(request).id
    if arg['user_id']:
        return redirect('/desirelist/%d/' % arg['user_id'])
    return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect('/')


@csrf_exempt
def register(request):
    arg = {}
    arg['master_id'] = request.GET.get('master_id', '')
    arg['sub_id'] = request.GET.get('sub_id', '')
    arg.update(csrf(request))
    arg['form'] = SignUpForm
    if request.POST:
        new_user_form = SignUpForm(request.POST)
        master_id = request.POST.get('master_id', '')
        sub_id = request.POST.get('sub_id', '')
        if new_user_form.is_valid():
            new_user_form.save()
            newuser = auth.authenticate(username=new_user_form.cleaned_data['username'], password=new_user_form.cleaned_data['password2'])
            auth.login(request, newuser)
            arg['user_id'] = auth.get_user(request).id
            if master_id != '':
                return redirect('/dreamers/%s/%s' % (master_id, sub_id))
            else:
                return redirect('/desirelist/%s' % arg['user_id'])
        else:
            if master_id != '':
                arg['password_error'] = '1'
                arg['error'] = new_user_form.errors
            else:
                arg['password_error'] = '1'
                arg['error'] = new_user_form.errors
                arg['form'] = new_user_form
    return render_to_response('register.html', arg)


