from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from .models import CoffeeShop


@admin.register(CoffeeShop)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')
