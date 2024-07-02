from django.contrib import admin
from django.urls import path, include
from .import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name="home"),
    path('login',views.loginhandle, name="loginhandle"),
    path('oklogin',views.loginHandleOK, name="loginOK"),
    path('capsules',views.publicCapsules,name="publicCapsules"),
    path('signup',views.signUphandle, name="signup"),   
    path('oksignup',views.signUphandleOK, name="signupOK"),
    path('logout', views.HandleLogout, name='HandleLogout'),
    path('privatecapsules',views.privateCapsules,name="privateCapsules"),
    path('privatecapsule/forceopen', views.ForceOpen, name="force-open"),
    path('capsules/data/<str:id>', views.publicData, name="public-data"),
    path('privatecapsule/data/<str:id>', views.privateData, name="private-data"),

    path('new-capsule', views.NewCapsule, name="new-capsule"),
    path('new-capsule-save', views.NewCapsuleSave, name="new-capsule-save"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
