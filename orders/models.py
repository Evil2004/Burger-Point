from asyncio.windows_events import NULL
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
import uuid
from cloudinary.models import CloudinaryField


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

class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = CloudinaryField("image")
    description = models.TextField(default = NULL)
    category = models.CharField(max_length=15)

    # It will return the name of the burger
    def __str__(self):
        return self.name

class Orders (models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Menu,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    order_date = models.DateField()

class Cart (models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Menu,on_delete=models.CASCADE)