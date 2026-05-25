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
#from django.contrib.auth import views as auth_views
from django.urls import path, include
# TODO: tarkista näiden kolmen sisältä ja oikea paikka
#from django.contrib.auth import views as auth_views
#from tilavaraus import views
#from django.views.generic import RedirectView

# Swagger / DRF
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger schema konfiguraatio
schema_view = get_schema_view(
   openapi.Info(
      title="Rajapintadokumentaatio",
      default_version='v1',
      description="Tilavarauksen API-dokumentaatio",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# TODO: tarkista kommentiksi muutetut auth.viewsit ja viewsit kumpaan urlspatternsiin kuuluu!
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tilavaraus.urls')), 
    #path('login/', auth_views.LoginView.as_view(template_name='tilavaraus/login.html'), name='login'),
    path('api/', include('tilavaraus.urls')),
    
    
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), 
    
    #path('testi/', auth_views.LoginView.as_view(template_name='tilavaraus/testi.html'),name='test'),
    #path('base/', auth_views.LoginView.as_view(template_name='tilavaraus/base.html'),name='base'),
    #path('home/', auth_views.LoginView.as_view(template_name='tilavaraus/home.html'),name='home'),
    #path('reservations/', auth_views.LoginView.as_view(template_name='tilavaraus/reservations.html'),name='reservations'),
    
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('login/', auth_views.LoginView.as_view(template_name='tilavaraus/login.html'),name='login'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='/login/'),name='logout'),
    # path('booking_list/', views.booking_list, name='booking_list'),
    # path('booking_detail/<int:bookingID>/',views.booking_detail, name='booking_detail'),
    # path('reservations/new/', views.create_booking, name='create_booking'),
    # path('edit_booking/<int:pk>/', views.edit_booking, name='edit_booking'),
    # path('delete_booking/<int:pk>/', views.delete_booking, name='delete_booking'),
                               
]
