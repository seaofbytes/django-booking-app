from datetime import datetime
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Q



# Create your models here.


class Apartment(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    apartment_price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    size = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    list_date = models.DateTimeField(default=datetime.now, blank=True)
        
    def price_by_date(self, date_obj, date_obj2):
        return self.price.filter(
                Q(price_start_date__lte=date_obj2) & Q(price_end_date__gte=date_obj)
            ).first()

    def __str__(self):
        return self.title

class ApartmentImages(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete="models.CASCADE", related_name="image")
    image = models.ImageField("image")

    def __str__(self):
        return self.image.url


class ApartmentPrices(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete="models.CASCADE", related_name="price")
    price_start_date = models.DateField(blank=True, null=True)
    price_end_date = models.DateField(blank=True, null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.apartment.title


class Reservation(models.Model):
    apartment = models.ForeignKey(Apartment, related_name='reservations',
                                  on_delete=models.CASCADE, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    name = models.CharField(default="", max_length=200)

    def __str__(self):
        return self.name
