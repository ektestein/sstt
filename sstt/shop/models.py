# from django.conf import settings
from django.db import models
from django.urls import reverse


class Product(models.Model):
    # COLOURS = (('black', 'black'), ('white', 'white'), ('red', 'red'))
    SIZES = (('XS', 'Extra small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'))
    image = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=2 ** 8)
    # category
    # colour = models.CharField(max_length=2 ** 3, choices=COLOURS)
    size = models.CharField(max_length=2, choices=SIZES)
    price = models.DecimalField(max_digits=9, decimal_places=2)  # сделать проверку на положительность

    def __str__(self):
        return self.name

    def get_absolute_ulr(self):
        return reverse('product-detail', args=[str(self.id)])


# class Basket(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL)
