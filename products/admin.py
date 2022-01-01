from django.contrib import admin
from .models import Product
# Register your models here.
from products.models import ProductReal


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Product, ProductAdmin)

admin.site.register(ProductReal)
