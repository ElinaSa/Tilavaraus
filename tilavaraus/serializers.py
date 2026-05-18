from rest_framework import serializers
from .models import Space, Booking
 
class SpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Space
        fields = ["room", "address", "location"]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["bookingID", "room", "email", "date", "begins", "ends"]

        extra_kwargs = {
            'bookingID': {'help_text': 'Varauksen tunnus'},
            'room': {'help_text': 'Varattu tila'},
            'email': {'help_text': 'Käyttäjätunnuksena oleva sähköpostiosoite'},
            'date': {'help_text': 'Päivä'},
            'begins': {'help_text': 'Aloitusaika'},
            'ends': {'help_text': 'Päättymisaika'},           
        }


 