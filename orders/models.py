from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
import uuid
from cloudinary.models import CloudinaryField


# Create your models here.

class Customer(AbstractUser):
    phone = models.CharField(max_length=15,default=None,unique=True)
    uuid = models.UUIDField(default=None,editable=False,unique=True)
    
    # remove unique constraint on username
    username = None
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True)
    
    REQUIRED_FIELDS = []
    
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
    image = CloudinaryField('image',folder='burger_point/images/')
    description = models.TextField(default = None)
    category = models.CharField(max_length=15)

    # It will return the name of the burger
    def __str__(self):
        return self.name


class Orders (models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Menu,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    order_date = models.DateField(default=None)
    order_time = models.TimeField(default=None)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

class Cart (models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Menu,on_delete=models.CASCADE)