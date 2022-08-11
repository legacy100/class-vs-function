from time import timezone
from django.db import models
import datetime 
from django.urls import reverse

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    # image_url = models.CharField(max_length=2083, null=True)
    image_url = models.ImageField(upload_to='images/', blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # def get_absolute_url(self):
    #     return reverse('product-detail', kwargs={'pk': self.pk})


    # def __str__(self):
    #     return self.name


class Offer(models.Model):
    code = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
