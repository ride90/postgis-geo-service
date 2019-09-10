from django.contrib.gis.db import models


class CoffeeShop(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    location = models.PointField()
