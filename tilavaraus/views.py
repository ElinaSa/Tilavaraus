from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Space, UserGroup, Person, Reservations
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return redirect('login')
    #return redirect('booking_list')
    

def login(request):
    return redirect('login')

def logout(request):
    return redirect('logout')

def testi(request):
    return redirect('testi')

def reservations(request):
    return redirect('reservations')

def booking_list(request):
    return HttpResponse("Tässä näkyvät varaukset")

def booking_detail(request):
    return HttpResponse("Tässä näkyvät varauksen yksityiskohdat")


# @login_required
# def booking_list(request):
    # return HttpResponse("Tässä näkyvät varaukset")
    # reservations=Reservation.objects.all()
    # return render(request, 'tilavaraus/booking_list.html',{'reservations':reservations})
# 
# def booking_detail(request, booking_id):
    # return HttpResponse(f"Varauksen ID: {booking_id}")