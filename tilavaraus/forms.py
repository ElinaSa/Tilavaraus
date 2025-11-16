from django import forms
from .models import Reservations, Space

class BookingForm(forms.ModelForm):

    # Suomalaiset aikaformaatit
    reservation_date = forms.DateField(
        input_formats=['%d.%m.%Y', '%Y-%m-%d'],
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    reservation_begins = forms.TimeField(
        input_formats=['%H.%M', '%H:%M'],
        widget=forms.TimeInput(attrs={'type': 'time'})
    )

    reservation_ends = forms.TimeField(
        input_formats=['%H.%M', '%H:%M'],
        widget=forms.TimeInput(attrs={'type': 'time'})
    )

    room = forms.ModelChoiceField(
        queryset=Space.objects.all(),
        empty_label="Valitse tila",
        widget=forms.Select()
    )

    class Meta:
        model = Reservations
        fields = ['room','reservation_date', 'reservation_begins', 'reservation_ends', 'reservation_id']

