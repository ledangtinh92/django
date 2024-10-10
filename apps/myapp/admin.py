from django.contrib import admin

from apps.myapp.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')


# Register your models here.
admin.site.register(Product, ProductAdmin)
