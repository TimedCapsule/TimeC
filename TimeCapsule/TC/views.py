from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, "TC/home.html")

def loginhandle(request):
    return render(request,"auth/login.html")

def signUphandle(request):
    return render(request,"auth/signup.html")