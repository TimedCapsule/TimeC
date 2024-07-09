from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import TimeCapsule, PublicCapsule
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
# Requirements for sending email...
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from TimeCapsule.settings import EMAIL_HOST_USER
from datetime import timedelta

def is_one_day_more(future_date, today_date):
    return future_date == today_date + timedelta(days=1)

def mailing():
    capsules = PublicCapsule.objects.all()
    
    for item in capsules:
        for x in item.contributers.all():
            today_date = datetime.date.today()
            is_Opening_Tomorrow = is_one_day_more(x.future_date.date(), today_date)
            
            if is_Opening_Tomorrow:
                subject = "Your TimeCapsule is Opening Tomorrow!"
                html_content = render_to_string("Mails/CapsOpenReminder.html", {
                    "title": x.title,
                    "username": x.user.username
                })
                text_content = strip_tags(html_content)
                recipient_list = [x.user.email]
                
                email = EmailMultiAlternatives(subject, text_content, EMAIL_HOST_USER, recipient_list)
                email.attach_alternative(html_content, "text/html")
                email.send()
    
    privCap = TimeCapsule.objects.all()
    
    for temp in privCap:
        today_date = datetime.date.today()
        is_Opening_Tomorrow = is_one_day_more(temp.future_date.date(), today_date)
        
        if is_Opening_Tomorrow:
            subject = "Your TimeCapsule is Opening Tomorrow!"
            html_content = render_to_string("Mails/CapsOpenReminder.html", {
                "title": temp.title,
                "username": temp.user.username
            })
            text_content = strip_tags(html_content)
            recipient_list = [temp.user.email]
            
            email = EmailMultiAlternatives(subject, text_content, EMAIL_HOST_USER, recipient_list)
            email.attach_alternative(html_content, "text/html")
            email.send()

mailing()

# Create your views here.

def home(request):
    return render(request, "TC/home.html")

def NewCapsule(request):
    # all_Users = User.objects.all()
    return render(request, "TC/NewCapsule.html")

def NewCapsuleSave(request):
    if(request.method == "POST"):
        caps_title = request.POST.get('title')
        caps_img1 = request.FILES.get('pic1')
        caps_img2 = request.FILES.get('pic2')
        caps_force_open_pass = request.POST.get('force_open_pass')
        caps_mssg = request.POST.get('message')
        caps_vid1 = request.FILES.get('vid1')
        caps_vid2 = request.FILES.get('vid2')
        caps_status = request.POST.get('status')
        caps_seal_date = request.POST.get('sealed_date')

        capsule = TimeCapsule(
            user = request.user,
            title = caps_title,
            status = caps_status,
            future_date = caps_seal_date,
            text = caps_mssg,
            force_open_pass = caps_force_open_pass,
            image1 = caps_img1,
            image2 = caps_img2,
            video1 = caps_vid1,
            video2 = caps_vid2,
            collaborators = request.user,
            is_sealed = True,
            is_force_opened = False
        )
        capsule.save()

        subject = "New Capsule is Created."
        html_content = render_to_string("Mails/NewCapsule.html",{
            "title": caps_title,
            "username": request.user.username,
        })
        text_content = strip_tags(html_content)
        recipient_list = [request.user.email]
        email = EmailMultiAlternatives(subject, text_content, EMAIL_HOST_USER, recipient_list)
        email.attach_alternative(html_content, "text/html")
        email.send()
        messages.success(request,"Capsule Created Successfully...")
        return redirect('publicCapsules')

def publicCapsules(request):
    capsules = PublicCapsule.objects.all()
    return render(request,'TC/Capsule.html',{'Capsule':capsules})

def publicCapsulesCollection(request,id):
    capsule = PublicCapsule.objects.get(id = id)
    contributers = capsule.contributers.all()
    today_date = datetime.date.today()
    cntxt = {'capsule':capsule,'contributers':contributers,'today_date':today_date}
    return render(request,"TC/capsuleCollection.html",cntxt)

def publicCapsulesCollectionData(request,id,pk):
    pub_cap = PublicCapsule.objects.get(id = id)
    cap_data = pub_cap.contributers.get(id = pk)
    cntxt = {"cap_data":cap_data}
    today_date = datetime.date.today()
    return render(request,"TC/CapsuleData.html",cntxt)

def privateCapsules(request):
    capsules = TimeCapsule.objects.filter(user = request.user)
    if(capsules is not None):
        privateCapsules = [cap for cap in capsules if cap.status == 'private']
        today_date = datetime.date.today()
    return render(request,'TC/privateCapsule.html',{'pc':privateCapsules,'today_date':today_date})

def ForceOpen(request):
    if request.method == 'POST':
        capsule_id = request.POST.get('force_open_id')
        capsule_pass = request.POST.get('force_open_password')

        capsule = TimeCapsule.objects.get(id = capsule_id)
        if(capsule.force_open_pass == capsule_pass):
            capsule.is_force_opened = True
            capsule.save()
            cntxt = {"capsuleData":capsule}
            messages.success(request,f'You Have Forcefully Opened the {capsule.title} Capsule....')
            return render(request,"TC/CapsuleData.html",cntxt)
        else:
            messages.error(request,"Provided Password is Wrong...")
            return redirect('privateCapsules')

def privateData(request,id):
    capsuleData = TimeCapsule.objects.get(id=id)
    cntxt = {"capsuleData":capsuleData}
    return render(request,"TC/CapsuleData.html",cntxt)

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

