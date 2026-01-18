from django.urls import path
from . import views
from .views import home, login, logout, reservations, booking_list, booking_detail, testi, create_booking, edit_booking, new_reservation
from rest_framework import permissions

urlpatterns = [
    path('',home, name='home'),
    path('',login,name='login'),
    path('',logout,name='logout'),
    path('',testi,name='testi'),
    path('',reservations,name='reservations'),
    path('reservations/',booking_list,name='booking_list'),
    path('reservations/',booking_detail,name='booking_detail'),
    path('reservations/',create_booking,name='create_booking'),
    path('reservations/',new_reservation,name='new_reservation'),  
    path("edit_booking/<int:pk>/", views.edit_booking, name="edit_booking"),

    # path('reservations/',edit_booking,name='edit_booking'),
    
    # path('reservations/edit_booking/<int:bookingID>',edit_booking, name='edit_booking'),
    # path('reservations/<int:bookingID>/edit_form',edit_booking,name='edit_booking'),
    # path('edit_booking/<int:bookingID>/', views.edit_booking, name='edit_booking'),
    # path('reservations/<int:booking_id>/',booking_detail,name='booking_detail'),
]
