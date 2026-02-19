from django.urls import path
from . import views
from .views import home, login, logout, reservations, booking_list, booking_detail, testi, create_booking, new_reservation, edit_booking, delete_booking
from rest_framework import permissions

urlpatterns = [
    path('',home, name='home'),
    path('',login,name='login'),
    path('',logout,name='logout'),
    path('',testi,name='testi'),
    path('',reservations,name='reservations'),
    path('reservations/',booking_list,name='booking_list'),
    path('reservations/<int:bookingID>/',booking_detail,name='booking_detail'),
    path('reservations/',create_booking,name='create_booking'),
    path('reservations/',new_reservation,name='new_reservation'),
    path('edit_booking/<int:pk>/', views.edit_booking, name='edit_booking'),
    path('delete_booking/<int:pk>/', views.delete_booking, name='delete_booking')
    

]
