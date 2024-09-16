from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Product, Order, Customer, Review

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Review)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'role',
                    'otp', 'otp_expires_at', 'is_confirmed')
    list_filter = ('role', 'is_confirmed')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(Customer, CustomerAdmin)
