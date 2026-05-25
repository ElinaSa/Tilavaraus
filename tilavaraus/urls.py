from django.urls import path
from . import views
from .views import home, login, logout, reservations, booking_list, booking_detail, create_booking, new_reservation, edit_booking, delete_booking
from .views import SpaceListAPI, BookingListAPI, BookingDetailAPI, TestAPIView




# Endpoints
urlpatterns = [
    
    path('',home, name='home'),
    path('',login,name='login'),
    #path('',logout,name='logout'),
    #path('',testi,name='testi'),
    
    path('reservations/',reservations,name='reservations'),
    path('reservations/',booking_list,name='booking_list'),
    path('reservations/<int:bookingID>/',booking_detail,name='booking_detail'),
    path('reservations/',create_booking,name='create_booking'),
    path('reservations/',new_reservation,name='new_reservation'),
    path('edit_booking/<int:pk>/', views.edit_booking, name='edit_booking'),
    path('delete_booking/<int:pk>/', views.delete_booking, name='delete_booking'),
    path("api/space/",SpaceListAPI.as_view(),name="space_list_api"),
    path("api/booking/",BookingListAPI.as_view(),name="booking_list_api"),
    path("api/booking/<int:pk>",BookingDetailAPI.as_view(),name="booking_detail_api"),
    path('test/', TestAPIView.as_view(),name='test-api'),
   
]
