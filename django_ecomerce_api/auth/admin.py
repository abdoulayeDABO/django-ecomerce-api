from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Product, Order, Customer, Review

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Review)
