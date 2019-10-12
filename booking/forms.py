
from django import forms
from django.forms.widgets import DateInput
from django.contrib.auth.models import User
from .models import Reservation
from bootstrap_datepicker_plus import DatePickerInput
from django.forms import ModelForm, TextInput


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

        # widgets = {
        #     'start_date': DateInput(attrs={'id': "datepicker"}),
        #     'end_date': DateInput(attrs={'id': 'datepicker'})

        # }
