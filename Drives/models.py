from __future__ import unicode_literals
from django.db import models
from Clients.models import Location


class Vehicle(models.Model):
    vehicleType = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField(default=50)

    class Meta:
        ordering = ['vehicleType']
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'

    def __str__(self):
        return self.vehicleType


class Driver(models.Model):
    name = models.CharField(verbose_name=u'Nome', max_length=100)
    email = models.EmailField(verbose_name=u'E-mail')
    contactNumberDDD = models.CharField(verbose_name=u'DDD', max_length=5)
    contactNumber = models.CharField(verbose_name=u'Numero Fixo', max_length=8, null=True, blank=True)
    contactNumberMobile = models.CharField(verbose_name=u'Numero Celular', max_length=9)
    categoryHab = models.CharField(verbose_name=u'Categoria Habilitação', max_length=2)
    location = models.ForeignKey(Location, verbose_name=u'Cidade', related_name="lacations")
    createdIn = models.DateField(auto_now=True, auto_now_add=False)
    vehicle = models.ManyToManyField(Vehicle, related_name="vehicles", verbose_name=u'Veiculos')


    class Meta:
        ordering = ['name']
        verbose_name = 'Driver'
        verbose_name_plural = 'Drivers'

    def __str__(self):
        return self.name