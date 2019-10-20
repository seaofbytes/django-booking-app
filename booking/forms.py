
from django import forms
from django.contrib.auth.models import User
from .models import Reservation
from django.forms import TextInput


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'start_date',
            'end_date',
            'name',
        ]
        widgets = {
            'start_date': TextInput(attrs={'id': 'datepicker'}),
            'end_date': TextInput(attrs={'id': 'datepicker2'}),
        }


