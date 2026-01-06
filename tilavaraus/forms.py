from django import forms
from django.core.exceptions import ValidationError
from .models import Booking, Space

class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ['room','date', 'begins', 'ends']

    # Päällekkäisten varausten esto
    def clean(self):
        cleaned_data = super().clean()
        date =cleaned_data.get('date')
        begins =cleaned_data.get('begins')
        ends =cleaned_data.get('ends')
        room =cleaned_data.get('room')

        if not date or not begins or not ends or not room:
            return cleaned_data
            
        if begins >= ends:
            raise ValidationError("Päättymisaika ei voi olla ennen alkamisaikaa.")
            
        overlapping = Booking.objects.filter(
            room=room,
            date=date,
            begins__lt=ends,
            ends__gt=begins
        )

        if self.instance.pk:
            overlapping = overlapping.exclude(pk=self.instance.pk)

        if overlapping.exists():
            raise ValidationError(
                "Tila on jo varattu valitulle ajankohdalle."
            )
            
        return cleaned_data

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

    
class BookingEditForm(forms.ModelForm):
    date = forms.DateField(
        input_formats=['%d.%m.%Y', '%Y-%m-%d'],
        label="Muokkaa päivä",
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    begins = forms.TimeField(
        input_formats=['%H.%M', '%H:%M'],
        label="Muokkaa aloitusaika",
        widget=forms.TimeInput(attrs={'type': 'time'})
    )
    ends = forms.TimeField(
        input_formats=['%H.%M', '%H:%M'],
        label="Muokkaa päättymisaika",
        widget=forms.TimeInput(attrs={'type': 'time'})
    )
    room = forms.ModelChoiceField(
        queryset=Space.objects.all(),
        label="Muokkaa tila",
        widget=forms.Select()
    ) 
    

