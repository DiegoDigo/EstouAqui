# coding=utf-8

from __future__ import unicode_literals
from django.db import models


class School(models.Model):
    schoolName = models.CharField(verbose_name=u'Nome Escola', max_length=100)
    publicPlaceNumber = models.CharField(verbose_name=u'Logradouro Numero', max_length=5)
    publicPlace = models.CharField(verbose_name=u'Logradouro', max_length=100)

    class Meta:
        ordering = ['schoolName']
        verbose_name = 'School'
        verbose_name_plural = 'Schools'

    def __str__(self):
        return self.schoolName


class Location(models.Model):
    cityName = models.CharField(verbose_name=u'Cidade', max_length=100)
    uf = models.CharField(verbose_name=u'uf', max_length=2)

    class Meta:
        ordering = ['cityName']
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __str__(self):
        return self.cityName


class Children(models.Model):
    name = models.CharField(verbose_name=u'Nome Filho', max_length=100)
    yearsOld = models.CharField(verbose_name=u'Idade', max_length=3)
    school = models.ForeignKey(School, verbose_name=u'Escola', related_name='schools')

    class Meta:
        ordering = ['name']
        verbose_name = 'Children'
        verbose_name_plural = 'Childrens'

    def __str__(self):
        return self.name


class Parents(models.Model):
    name = models.CharField(verbose_name=u'Nome', max_length=100)
    email = models.EmailField(verbose_name=u'Email')
    publicPlace = models.CharField(verbose_name=u'Logradouro', max_length=100)
    numberPublicPlace = models.CharField(verbose_name=u'Logradouro Numero', max_length=10)
    contactNumberDDD = models.CharField(verbose_name=u'DDD', max_length=5)
    contactNumber = models.CharField(verbose_name=u'Numero Fixo', max_length=8, null=True, blank=True)
    contactNumberMobiel = models.CharField(verbose_name=u'Numero Celular',max_length=9)
    createdIn = models.DateField(auto_now=True, auto_now_add=False)
    children = models.ManyToManyField(Children, verbose_name=u'Filhos', related_name='childrens')
    location = models.ForeignKey(Location, verbose_name=u'Cidade',related_name='locations')

    class Meta:
        ordering = ['name']
        verbose_name = 'Parents'
        verbose_name_plural = 'Parents'

    def __str__(self):
        return self.name