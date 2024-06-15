from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import TimeCapsule
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
# Create your views here.

def home(request):
    return render(request, "TC/home.html")

def publicCapsules(request):
    capsules = TimeCapsule.objects.all()
    #print(capsules)
    if(capsules is not None):
        publicCapsules = {cap for cap in capsules if cap.status == 'public'}
        for i in publicCapsules:
            print(i.future_date.date())
            print(i.future_date.time())
        today_date = datetime.date.today()
    return render(request,'TC/Capsule.html',{'pc':publicCapsules,'today_date':today_date})

def privateCapsules(request):
    capsules = TimeCapsule.objects.all()
    if(capsules is not None):
        privateCapsules = [cap for cap in capsules if cap.status == 'private']
        today_date = datetime.date.today()
    return render(request,'TC/privateCapsule.html',{'pc':privateCapsules,'today_date':today_date})


def loginhandle(request):
    return render(request,"auth/login.html")

def signUphandle(request):
    return render(request,"auth/signup.html")

def signUphandleOK(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(username) > 12:
            messages.warning(request, "Username must be under 12 characters !!!")
            return redirect('signup')
        
        if not username.isalnum():
            messages.warning(request, "Username should only contain letters and numbers !!!")
            return redirect('signup')

        if pass1 != pass2:
            messages.warning(request, "Passwords do not match")
            return redirect('signup')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.email = email
        myuser.save()
        messages.success(request, "Your Account has been Successfully created...")
        return redirect('loginhandle')
    else:
        return(HttpResponse, "404 - NOT Found")
    
def loginHandleOK(request):
    if request.method == 'POST':
        loginusername = request.POST['username']
        loginpassword = request.POST['password']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully LoggedIn...")
            return redirect('home')
        else:
            messages.error(request, "Invalid Login Credentials...")
            return redirect('loginhandle')
        
def HandleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out...")
    return redirect('home')

