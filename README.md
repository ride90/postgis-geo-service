# postgis-geo-service
### Location based service built using PostgreSQL, PostGIS and GeoDjango.

It's a simple app used as a playground to see what I can achieve using PostGIS.

## Links

- [python3](https://docs.python.org/3/)
- [GeoDjango](https://docs.djangoproject.com/en/2.2/ref/contrib/gis/)
- [PostGIS](https://postgis.net/)

## Installation

- [Geospatial libraries](https://docs.djangoproject.com/en/2.2/ref/contrib/gis/install/geolibs/)
- [PostGIS](https://docs.djangoproject.com/en/2.2/ref/contrib/gis/install/postgis/)

This app is tiny, so I'm not going to describe how to install a django app, just `venv` with `python3` and `pip install` requirements and `run migrations` and you are fine., and don't forget to create a db/user and set in settings.

P.S. There is a docker image with postgresql and postgis configured here: https://hub.docker.com/r/kartoza/postgis/

## Dataset
I've downloaded information about all `coffee places in Prague` from https://www.openstreetmap.org as a dataset to use.
There is a data migration which will fullfill db. 

## Endpoints

### Get closest coffee places from Old Town Square
`/coffee/closest`
