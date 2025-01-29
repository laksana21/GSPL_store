# Django library
from django.contrib import admin

# Project library
from .models import Product

# Admin Interview settings
class ProductAdmin(admin.ModelAdmin):
    list_display = ['Id', 'name', 'description', 'price', 'created_at', 'updated_at']
    list_filter = ['name', 'price', 'created_at', 'updated_at']
    search_fields = ['name', 'description', 'price', 'created_at', 'updated_at']

# Register your models here.
admin.site.register(Product, ProductAdmin)
