from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import TimeCapsule
# Create your views here.

def home(request):
    return render(request, "TC/home.html")

def viewCapsules(request):
    capsules = TimeCapsule.objects.all()
    publicCapsules = [cap for cap in capsules if cap.status is 'public']
    print(publicCapsules)
    return HttpResponse('ok')
