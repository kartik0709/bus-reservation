from django import forms

class FindReservation(forms.Form):
    ticket_number = forms.CharField(max_length=255)
    