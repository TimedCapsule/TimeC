from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import TimeCapsule
# Create your views here.

def home(request):
    return render(request, "TC/home.html")

def publicCapsules(request):
    capsules = TimeCapsule.objects.all()
    #print(capsules)
    if(capsules is not None):
        publicCapsules = [cap for cap in capsules if cap.status == 'public']
    return render(request,'TC/Capsule.html',{'pc':publicCapsules})

def privateCapsules(request):
    capsules = TimeCapsule.objects.all()
    if(capsules is not None):
        privateCapsules = [cap for cap in capsules if cap.status == 'private']
    return render(request,'TC/privateCapsule.html',{'pc':privateCapsules})


def loginhandle(request):
    return render(request,"auth/login.html")

def signUphandle(request):
    return render(request,"auth/signup.html")