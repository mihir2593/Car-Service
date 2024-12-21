from django.contrib.auth import logout
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from storesapp import models


# Create your views here.
def index(request):
    return render(request, 'admin/index.html')


def adminregister(request):
    if request.method == "POST":
        if request.POST.get('password') == request.POST.get('password1'):
            try:
                User.objects.get(username=request.POST.get('username'))
                return HttpResponse ("user is already exist")
            except:
                user = User.objects.create_user(username=request.POST.get('username'),
                                                email=request.POST.get('email'),
                                                password=request.POST.get('password'))
                return redirect(adminlogin)
        else:
            return HttpResponse ("Enter Valid Password")
    return render(request, 'admin/pages-register.html')





def adminlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect (index)
        else:
            return HttpResponse ("User is not found ")
    return render(request, 'admin/pages-login.html')


def adminlogout(request):
    logout(request)
    return redirect(adminlogin)

