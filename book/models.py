from django.db import models
from django.contrib.auth.models import User
from web.models import Bus, Route
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .seatingpattern import SEATING_ARRAYS
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator

class Seat(models.Model):
    class Meta:
        verbose_name_plural = "Seat"
    id = models.AutoField(primary_key=True,)
    position = models.CharField(max_length=4)
    bus = models.ForeignKey(Bus)
    status = models.CharField(max_length=20, choices=(('available', 'available'), ('reserved', 'reserved'), ('unavailable', 'unavailable'),), default='available')
    seat_label = models.IntegerField()
	
	
    def __str__(self):
        return '{0}-{1}-{2}'.format((self.bus),(self.id),(self.status))
    
@receiver(post_save, sender=Bus)
def create_seats(sender, instance, created, **kwargs):
    if created:
        label = 0
        seating_pattern = SEATING_ARRAYS[instance.seating_pattern]
        for row,seats in enumerate(seating_pattern):
            for pos,seat in enumerate(seats):
                if seat:
                    label = label + 1
                    Seat.objects.create(
                        bus=instance,
                        position="{}_{}".format(str(row+1), str(pos+1)),
                        seat_label="{}".format(label)
                    )

class Booking(models.Model):
    class Meta:
        verbose_name_plural = "Booking"
    user = models.ForeignKey(User, null=True)
    #session = models.ForeignKey(sessions.Sessions)
    name = models.CharField(max_length=100,)
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female'),), default='')
    age = models.IntegerField()
    phone = models.IntegerField()
    seat = models.OneToOneField(Seat)

    def __str__(self):
        return '{0}{1}-{2}'.format((self.user),(self.name),(self.seat))
 
class Ticket(models.Model):
    class Meta:
        verbose_name_plural = "Ticket"
    book = models.OneToOneField(Booking)
       
    def __str__(self):
        return '{0}-{1}'.format((self.book), (self.id),)