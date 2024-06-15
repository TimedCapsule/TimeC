from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('',views.home, name="home"),
    path('login',views.loginhandle, name="loginhandle"),
    path('publiccapsules/',views.publicCapsules,name="publicCapsules"),
    path('privatecapsules/',views.privateCapsules,name="privateCapsules"),
]
