from django.shortcuts import render, reverse, redirect
from accounts.forms import UserLoginForm, UserRegistrationForm
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from checkout.models import Order


def index(request):
    """Return index.html file"""
    return render(request, 'index.html')


@login_required
def user_logout(request):
    logout(request)
    messages.success(
                    request, "You have successfully logged out. See you again!")
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserRegistrationForm(data=request.POST)

        if user_form.is_valid():
            user_form.save()
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])

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
            name = request.user.username
            messages.success(
                    request, "You have successfully registered. Welcome %s!" % name)
            return redirect(reverse('index'))
    else:
        if request.user.is_authenticated:
            registered = True
        user_form = UserRegistrationForm()

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
            name = request.user.username
            messages.success(
                    request, "Welcome %s." % name)
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponse("Your account was inactive.")
    else:
        print("You have to register your account first in order to login!")
        return HttpResponseRedirect(reverse('register'))

@login_required
def user_profile(request):
    orders = Order.objects.filter(user=request.user).order_by('-date')
    return render(request, 'profile.html', {'orders': orders})
