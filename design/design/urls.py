"""
URL configuration for design project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.accounts.views import SignInView, SignUpView, MainView, LogOutView
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", SignInView.as_view(), name="auth"),
    path("reg/", SignUpView.as_view(), name="reg"),
    path("logout/", LogOutView.as_view(), name="logout"),
    path("", MainView.as_view(), name="main"),
    path("lk/", TemplateView.as_view(template_name="accounts/lk.html")),
    
]
