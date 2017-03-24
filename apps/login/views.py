from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
import re
import bcrypt
password = "kittens"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
    return render(request, 'login/index.html')

def register(request):
    if request.method == "POST":
        validation = User.objects.regVal(request.POST)

        if validation[0]:
            request.session['current_user']=validation[1].first_name
            return redirect("login:success")
        else:
            for error in validation[1]:
                messages.error(request, error)
            return redirect('login:index')
    return redirect('login:index')

def login(request):
    if request.method == "POST":
        validation = User.objects.logVal(request.POST)

        if validation[0]:
            request.session['current_user']=validation[1].first_name
            return redirect("login:success")
        else:
            for error in validation[1]:
                messages.error(request, error)
            return redirect('/')
    return redirect('login:index')

def success(request):
    if not "current_user" in request.session:
        messages.add_message(request, messages.INFO, "Must be logged in to view this page")
        return redirect('login:index')
    else:
        return render(request, "login/success.html")

def logout(request):
    request.session.clear()
    return redirect('login:index')
