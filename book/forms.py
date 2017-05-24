from django import forms
from . import models
from django.forms import formset_factory

class FormBookBus(forms.ModelForm):
    class Meta:
        model = models.Booking
        fields = [
            'name',
            'gender',
            'age',
            'phone',
         ]

