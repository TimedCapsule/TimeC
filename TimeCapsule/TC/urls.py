from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('',views.home, name="home"),
    path('login',views.loginhandle, name="loginhandle"),
    path('oklogin',views.loginHandleOK, name="loginOK"),
    path('capsules',views.viewCapsules,name="viewCapsules"),
    path('signup',views.signUphandle, name="signup"),
    path('oksignup',views.signUphandleOK, name="signupOK"),
    path('logout', views.HandleLogout, name='HandleLogout'),
]
