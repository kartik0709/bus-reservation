from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . import forms
from .models import Bus
import calendar
from datetime import datetime


 
@login_required
def user_profile(request):
    user = request.user
    context = {'user': user}
    template = 'profile.html'
    return render(request, template, context)
 
def find_bus(request):
    form = forms.FormFindBus
        
    template = 'home.html'
    context = {'form': form}
    return render(request, template, context)


 
def select(request):

    bus_type = request.GET.get('bus_type')
    #qs = Bus.objects.filter(type_of_bus=bus_type)

    bus_from = request.GET.get('bus_from')
    #qs = Bus.objects.filter(route__location_from=bus_from)
    
    bus_to = request.GET.get('bus_to')
    #qs = qs.filter(route__location_to=bus_to)
    
    date_string = request.GET.get('date')
    
    request.session['bus_from'] = bus_from
    request.session['bus_to'] = bus_to
    request.session['date'] = date_string

    qs = Bus.objects.filter(type_of_bus=bus_type, route__location_from=bus_from, route__location_to=bus_to, date=date_string)

        
    context = {'qs': qs,}
    template = 'select.html'
    return render(request, template, context)