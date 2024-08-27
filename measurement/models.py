from django.db import models
from django.forms.fields import ImageField



class Sensor(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()

class Measurement(models.Model):

    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(decimal_places=1, max_digits=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


