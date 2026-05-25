from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Space, Booking
from .forms import BookingForm, BookingEditForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from .serializers import SpaceSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class TestAPIView(APIView):
    """
    API-testi
    """
    def get(self, request):
        return Response({
            "message": "Swagger toimii"
        })
    
class SpaceListAPI(generics.ListAPIView):
    """
    Varausten hallinta-API: varattavien tilojen listaus
    """
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer
    permission_classes = [IsAuthenticated]

class BookingListAPI(generics.ListCreateAPIView): #viewsets.ReadOnlyModelViewSet
    """
    Varausten hallinta-API: tehtävien listaus ja lisääminen
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return Booking.objects.all()
        return Booking.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BookingDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    

#@login_required
#def home(request):
    
    # return redirect('home') 
    #return redirect('login')
    # TODO: Tässä home aiheuttaa virheen
    
#@login_required
def login(request):
    return redirect('reservations')

@login_required
def logout(request):
    return redirect('logout')

@login_required
def testi(request):
    return redirect('testi')

@login_required
def reservations(request):
    return redirect('reservations')

#@login_required
# def booking(request):
    # return redirect('new_reservation')

@login_required
def booking_list(request):
    now = timezone.now()

    # käyttäjän varaukset
    bookings = Booking.objects.filter(email=request.user)


    upcoming = bookings.filter(date__gte=now).order_by('begins')
    past = bookings.filter(date__lt=now).order_by('-begins')

    return render(request, "tilavaraus/booking_list.html", {
        'bookings': bookings,
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

@login_required
def edit_booking(request, pk):

    booking = get_object_or_404(
        Booking, 
        pk=pk, 
        email=request.user, # käyttäjä saa muokata vain omia varauksia
        date__gte=timezone.now().date() # vain tulevat varaukset
    )
   
    if request.method == "POST":
        form = BookingEditForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingEditForm(instance=booking)

    return render(request, "tilavaraus/edit_booking.html", {
        'form':form,
        'booking': booking
    })

@login_required
def delete_booking(request, pk):

    booking = get_object_or_404(
        Booking, 
        pk=pk, 
        email=request.user, # käyttäjä saa poistaa vain omia varauksia
        date__gte=timezone.now().date() # vain tulevat varaukset
    )
    booking.delete()
    return redirect('booking_list')


@login_required
def booking_detail(request,bookingID):
    return HttpResponse(f"Varauksen ID: {bookingID}")
# booking.bookingID
# 
@login_required
def new_reservation(request):
    return HttpResponse("Tässä uusin varaus")
