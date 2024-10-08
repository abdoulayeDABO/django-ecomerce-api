from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
import datetime


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    in_stock = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products', null=True)
    created_at = models.DateTimeField(auto_now=True, null=True)
    image_url = models.CharField(null=True)

    def __str__(self):
        return self.name


class OrderStatus(models.TextChoices):
    DELIVERED = 'delivered', 'Delivered'
    RECEIVED = 'received', 'Received'
    PROCESSING = 'processing', 'Processing'


class Order(models.Model):
    date = models.DateTimeField(default=timezone.now)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    amount = models.IntegerField()
    status = models.CharField(max_length=50, choices=OrderStatus.choices)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.id} by {self.customer}"


class Role(models.TextChoices):
    USER = 'user', 'User'
    ADMIN = 'admin', 'Admin'


class Customer(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(
        max_length=50, choices=Role.choices, default=Role.USER)
    password = models.CharField(max_length=255)
    is_confirmed = models.BooleanField(default=False)
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)
    is_confirmed = models.BooleanField(default=False)
    otp = models.CharField(max_length=4, null=True)
    otp_expires_at = models.DateTimeField(null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email


class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    content = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"Review by {self.customer} on {self.product}"
