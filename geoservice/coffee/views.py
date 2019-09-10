from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance

from .models import CoffeeShop


# for demo it's fine to hardcode it :)
# this coordinates point to Old Town Square in Prague
latitude = 50.087623
longitude = 14.420339
location = Point(longitude, latitude, srid=4326)


class ClosestCoffeeShops(generic.ListView):
    model = CoffeeShop
    context_object_name = 'coffee_shops'
    template_name = 'nerby_demo.html'
    queryset = CoffeeShop.objects.annotate(
        distance=Distance('location', location)
    ).order_by('distance')[0:50]