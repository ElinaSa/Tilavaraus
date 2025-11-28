from django.urls import path
from .views import home, login, logout, reservations, booking_list, booking_detail, testi, create_booking, new_reservation
from rest_framework import permissions

urlpatterns = [
    path('',home, name='home'),
    path('',login,name='login'),
    path('',logout,name='logout'),
    path('',testi,name='testi'),
    path('',reservations,name='reservations'),
    path('reservations/',booking_list,name='booking_list'),
    path('reservations/',booking_detail,name='booking_detail'),
    path('reservations/', create_booking,name='create_booking'),
    path('reservations/',new_reservation,name='new_reservation'),
    # path('reservations/<int:booking_id>/',booking_detail,name='booking_detail'),
]
