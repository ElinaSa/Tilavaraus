from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Reservation

# Create your views here.
def home(request):
    #return redirect('booking_list')
    return HttpResponse("Raseko Goes Virtual! Tervetuloa tilavarausjärjestelmään")

def booking_list(request):
    #return HttpResponse("Tässä näkyvät varaukset")
    reservations=Reservation.objects.all()
    return render(request, 'tilavaraus/booking_list.html',{'reservations':reservations})

def booking_detail(request, booking_id):
    return HttpResponse(f"Varauksen ID: {booking_id}")