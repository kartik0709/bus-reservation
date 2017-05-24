from django.contrib import admin
from . import models

admin.site.register(models.Booking)
admin.site.register(models.Seat)
admin.site.register(models.Ticket)
