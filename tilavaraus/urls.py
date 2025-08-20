from django.urls import path
from .views import home, login, booking_list, booking_detail
from rest_framework import permissions

urlpatterns = [
    path('',home, name='home'),
    path('',login,name='login'),
    path('reservations/',booking_list,name='booking_list'),
    path('reservations/<int:booking_id>/',booking_detail,name='booking_detail'),
]
