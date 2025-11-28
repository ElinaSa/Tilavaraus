from django import forms
from .models import Booking, Space

class BookingForm(forms.ModelForm):

    # Suomalaiset aikaformaatit
    date = forms.DateField(
        input_formats=['%d.%m.%Y', '%Y-%m-%d'],
        label="Valitse päivä",
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    begins = forms.TimeField(
        input_formats=['%H.%M', '%H:%M'],
        label="Aloitusaika",
        widget=forms.TimeInput(attrs={'type': 'time'})
    )

    ends = forms.TimeField(
        input_formats=['%H.%M', '%H:%M'],
        label="Päättymisaika",
        widget=forms.TimeInput(attrs={'type': 'time'})
    )

    room = forms.ModelChoiceField(
        queryset=Space.objects.all(),
        label="Valitse tila",
        widget=forms.Select()
    )

    class Meta:
        model = Booking
        fields = ['room','date', 'begins', 'ends']

