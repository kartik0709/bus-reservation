from django.db import models
from django.core.exceptions import ValidationError


class Route(models.Model):
    class Meta:
        verbose_name_plural = "Routes"
        
    BUSFROM = (
    ('Delhi', 'Delhi'),
    ('Jaipur', 'Jaipur'),
    ('Ajmer', 'Ajmer'),
    )

    BUSTO = (
    ('Ajmer', 'Ajmer'),
    ('Chandigarh', 'Chandigarh'),
    ('Delhi', 'Delhi'),
    )
    
    route_id = models.AutoField(primary_key=True,)    
    location_from = models.CharField(max_length=255, choices=BUSFROM)
    location_to = models.CharField(max_length=255,choices=BUSTO)        
    
    def __str__(self):
        if self.location_from == self.location_to:
            raise ValidationError('To and From Can\'t be the same')
        return '{0}-{1}'.format(str(self.location_from), str(self.location_to))
        

class Bus(models.Model):
    
    BUSTYPE = (
    ('Volvo', 'Volvo'),
    ('Ordinary', 'Ordinary'),
    )
	
    SEATING_PATTERNS = (
    ('BUS_35', 'BUS_35'),
    ('BUS_31', 'BUS_31'),
    )
	
    class Meta:
        verbose_name_plural = "Bus"
    id = models.AutoField(primary_key=True,)
    type_of_bus = models.CharField(max_length=255, choices=BUSTYPE)
    bus_registration = models.CharField(max_length=255, default='')
    capacity = models.CharField(max_length=2, choices=(('35', '35'), ('31', '31'),))
    price = models.IntegerField()
    bus_number = models.IntegerField(unique=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    route = models.ForeignKey(Route,)    
    seating_pattern = models.CharField(choices=SEATING_PATTERNS, max_length=50,)
    
    def __str__(self):
        return '{0}, {1}, {2}-{3}'.format(str(self.bus_number), self.type_of_bus, self.route, self.date)
    
