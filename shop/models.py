from django.db import models
from alcoldrinks.models import AlcolDrinks
# Create your models here.

class AllShop(models.Model):
    CHOICE = {
        ('patner','파트너'), ('store','스토어')
    }
    name = models.CharField(max_length=100);
    location = models.CharField(max_length=100);
    alcolshoptype = models.CharField(max_length=20, choices=CHOICE, default='patner')

class Filter(models.Model):
    patner = models.BooleanField(default='True')
    store = models.BooleanField(default='True')
    
class ShopDrinks_Count(models.Model):
    shop = models.ForeignKey(AllShop, on_delete=models.CASCADE)
    drinks = models.ForeignKey(AlcolDrinks, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
