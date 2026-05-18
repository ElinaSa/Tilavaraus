from django.urls import path
from . import views
from .views import home, login, logout, reservations, booking_list, booking_detail, testi, create_booking, new_reservation, edit_booking, delete_booking, SpaceListAPI, BookingListAPI, BookingDetailAPI
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.views.generic import RedirectView

schema_view = get_schema_view(
   openapi.Info(
      title="Rajapintadokumentaatio",
      default_version='v1',
      description="Tilavarauksen API",
      terms_of_service="https://google.com/policies/terms/",
      contact=openapi.Contact(email="contact@tilavaraus.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

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
    path('delete_booking/<int:pk>/', views.delete_booking, name='delete_booking'),
    path("api/space/",SpaceListAPI.as_view(),name="space_list_api"),
    path("api/booking/",BookingListAPI.as_view(),name="booking_list_api"),
    path("api/booking/<int:pk>",BookingDetailAPI.as_view(),name="booking_detail_api"),
    #path('admin/', admin.site.urls),
    #path('api/', include('booking.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), 
    #path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]