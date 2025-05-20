from django.urls import path
from .views import home, booking_list, booking_detail

urlpatterns = [
    path('',home, name='home'),
    path('reservations/',booking_list,name='booking_list'),
    path('reservations/<int:booking_id>/',booking_detail,name='booking_detail'),
]