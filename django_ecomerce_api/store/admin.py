from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Product, Order, Customer, Review

admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Review)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'description',
                    'price',
                    'category',
                    'in_stock',
                    'created_at',
                    'image_url',
                    'image'
                    )
    list_filter = ('category', 'in_stock')
    search_fields = ('name', 'description', 'category')
    ordering = ('name',)


admin.site.register(Product, ProductAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('email',
                    'first_name',
                    'last_name',
                    'password',
                    'created_at',
                    'updated_at',
                    'country',
                    'city',
                    'role',
                    'otp',
                    'otp_expires_at',
                    'is_confirmed')

    list_filter = ('role', 'is_confirmed')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(Customer, CustomerAdmin)
