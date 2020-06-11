from django.shortcuts import render, reverse, redirect
from accounts.forms import UserForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
    """Return index.html file"""
    return render(request, 'index.html')



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            # We need to authenticate a user, otherwise the system will show him the 'register' route
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            '''
                The best practice of authentication is to redirect a user to a new page. If we try to stay at the
                same page, we get POST requests when an auth form is not filled completely and we try to reload the
                page. We expect GET requests but get POST ones.  
            '''
            return redirect(reverse('thanks'))
        else:
            print(user_form.errors)
    else:
        if request.user.is_authenticated:
            registered = True
        user_form = UserForm()

    return render(request, 'registration.html',
                           {'user_form': user_form,
                            'registered': registered})


def thank_you(request):
    return render(request, 'thank_you.html')


def user_login(request):
    if request.method == 'POST':
        return authenticate_user(request, request.POST.get('username'), request.POST.get('password'))
    else:
        login_form = UserLoginForm()
        return render(request, 'login.html', {"login_form": login_form})


def authenticate_user(request, username, password):
    user = authenticate(username=username, password=password)
    if user:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponse("Your account was inactive.")
    else:
        print("You have to register your account first in order to login!")
        return HttpResponseRedirect(reverse('register'))


def user_profile(request):
    return render(request, 'profile.html')