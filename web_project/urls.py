"""
URL configuration for web_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from tilavaraus import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('testi/', auth_views.LoginView.as_view(template_name='tilavaraus/testi.html'),name='test'),
    path('base/', auth_views.LoginView.as_view(template_name='tilavaraus/base.html'),name='base'),
    path('home/', auth_views.LoginView.as_view(template_name='tilavaraus/home.html'),name='home'),
    path('reservations/', auth_views.LoginView.as_view(template_name='tilavaraus/reservations.html'),name='reservations'),
    path('', include('tilavaraus.urls')), 
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='tilavaraus/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'),name='logout'),
    path('booking_list/', views.booking_list, name='booking_list'),
    path('reservations/new/', views.create_booking, name='create_booking'),
    
    
]
