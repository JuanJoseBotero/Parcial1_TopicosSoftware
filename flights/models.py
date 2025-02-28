from django.db import models

# Create your models here.


class Flight(models.Model):
    name = models.CharField(max_length=100)
    flight_type = models.CharField(max_length=100, default='Nacional')  
    price = models.FloatField()
    
    def __str__(self):
        return self.name