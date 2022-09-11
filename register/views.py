from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages


def register(req):
    if req.method == 'POST':
        form = RegisterForm(req.POST)
        if form.is_valid():
            new_user = form.save()
            messages.info(req, "Thanks for registering. You are now logged in.")
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            auth_login(req, new_user)
            return render(req, 'successRegister.html', {})
        
    form = RegisterForm(req.POST or None)
    return render(req, 'register.html', {"form": form})


def login(req):
    pass
