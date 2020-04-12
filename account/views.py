from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django import forms
# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'This Email address already Exist!')
                return redirect('register')
            else:
                user = User.objects.create_user(username = email, first_name = first_name, last_name = last_name, email = email, password = password )
                user.save()
                messages.info(request, 'An Account has been Created')
                return redirect('login')
        else:
            messages.error(request, 'Passwords Does not Match!')   
            return redirect('register')

    else:
        return render(request, 'signUp.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username = email, password = password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are Logged in!')
            next = request.META['HTTP_REFERER']
            return HttpResponseRedirect(next)
        else:
            messages.error(request, 'Invaild Credentials')
            return redirect('login')
    else:
        return render(request, 'signIn.html')

def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully been Logged Out')
    return redirect('login')