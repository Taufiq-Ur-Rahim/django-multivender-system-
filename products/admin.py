from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'vendor', 'created_at']
    list_filter = ['category', 'vendor']
    search_fields = ['name', 'description']
