from django.contrib import admin

# Register your models here.
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_title','product_price','product_desc')
    search_fields = ('product_title','product_price','product_desc')

admin.site.register(Product,ProductAdmin)

