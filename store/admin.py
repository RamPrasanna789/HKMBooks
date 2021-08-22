from django.contrib import admin
from django.db import models
from .models import Product, Variation

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name']
    prepopulated_fields = {'slug': ('product_name',)}

class VariationAdmin(admin.ModelAdmin):
    list_display = ['product', 'variation_category', 'is_active', 'variation_value']
    list_editable = ['is_active', 'variation_value']
    list_filter = ['product', 'variation_category', 'is_active', 'variation_value']
admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)