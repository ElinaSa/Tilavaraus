from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Space, Booking
from .forms import BookingForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from rest_framework.permissions import IsAuthenticated

# Create your views here.

@login_required
def home(request):
    
    # return redirect('home') 
    return redirect('login')
    # TODO: Tässä home aiheuttaa virheen
    
@login_required
def login(request):
    return redirect('login')

@login_required
def logout(request):
    return redirect('logout')

@login_required
def testi(request):
    return redirect('testi')

@login_required
def reservations(request):
    return redirect('reservations')

@login_required
# def booking(request):
    # return redirect('new_reservation')

@login_required
def booking_list(request):
    now = timezone.now()

    # käyttäjän varaukset
    bookings = Booking.objects.filter()


    upcoming = bookings.filter(date__gte=now).order_by('begins')
    past = bookings.filter(date__lt=now).order_by('-begins')

    return render(request, "tilavaraus/booking_list.html", {
        # 'bookings': bookings,
        "upcoming": upcoming,
        "past": past,
    })

    # bookings = Booking.objects.all().order_by('date', 'begins')
    # return render(request, 'tilavaraus/booking_list.html', {'bookings': bookings})

    # return HttpResponse("Tässä näkyvät varaukset")
# 
@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.email = request.user
            booking.save()
            return redirect('booking_list')
    else:
        form = BookingForm()

    return render(request, 'tilavaraus/create_booking.html', {'form': form})
# TODO:Tarkista onko create_bookin oikea osoite tässä
# 
@login_required
def booking_detail(request):
    return HttpResponse("Tässä näkyvät varauksen yksityiskohdat")

@login_required
def new_reservation(request):
    return HttpResponse("Tässä uusin varaus")

# @login_required
# def booking_list(request):
    # return HttpResponse("Tässä näkyvät varaukset")
    # reservations=Reservation.objects.all()
    # return render(request, 'tilavaraus/booking_list.html',{'reservations':reservations})

# def booking_detail(request, booking_id):
    # return HttpResponse(f"Varauksen ID: {booking_id}")