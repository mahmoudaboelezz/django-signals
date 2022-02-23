from re import T
from django.db import models
import cars
from cars.models import Car

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=200)
    cars = models.ManyToManyField(Car)
    total = models.PositiveIntegerField(blank=True,null=True)
    total_price = models.PositiveIntegerField(blank=True,null=True)
    active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return str(self.name)