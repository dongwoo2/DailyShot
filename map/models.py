from django.db import models

# Create your models here.
class Alcolshop(models.Model):
    name = models.CharField(max_length=70)
    location = models.CharField(max_length=70, default='')

    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)