from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class Customer(AbstractUser):
    phone = models.CharField(max_length=15,default=None,unique=True)
    uuid = models.UUIDField(default=None,editable=False,unique=True)
    def __str__(self):
        return self.username

class Address(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pin = models.CharField(max_length=10)

    def __str__(self):
        return self.address

class Burger(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='burger_images')

    # It will return the name of the burger
    def __str__(self):
        return self.name