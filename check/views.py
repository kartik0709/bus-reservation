from django.shortcuts import render
from . import forms
from book.models import Ticket

def check_reservation(request):
    form = forms.FindReservation
    
    template = 'check_reservation.html'
    context = {'form': form}
    return render(request, template, context)

def show_ticket(request):

    ticket_no = request.GET.get('ticket_number')
    
    query = []
    
    for letter in ticket_no[::-1]:
        if letter=='-':
            break
        query.append(letter)
        
    stringq = ''.join(query)
    
    qs = Ticket.objects.filter(id=stringq)
    
    context = {'qs': qs}
    template = 'ticket.html'
    return render(request, template, context)