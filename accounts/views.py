from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def login_view(request):

    if request.method=="POST":

        username=request.POST["username"]
        password=request.POST["password"]

        user=authenticate(request,username=username,password=password)

        if user:
            login(request,user)
            return redirect("dashboard")

        messages.error(request,"Invalid login")

    return render(request,"login.html")


def register_view(request):

    if request.method=="POST":

        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]

        User.objects.create_user(username,email,password)

        return redirect("login")

    return render(request,"register.html")


@login_required
def dashboard(request):
    return render(request,"dashboard.html")


@login_required
def profile(request):
    return render(request,"profile.html")


def logout_view(request):

    logout(request)
    return redirect("login")