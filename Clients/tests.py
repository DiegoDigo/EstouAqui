from model_mommy import mommy
from django.test import TestCase
from django.utils.timezone import datetime
from .models import School, Location, Children, Parents


class TestSchool(TestCase):

    def setUp(self):
        self.scholl = mommy.make(School, schoolName="Luiza Salete Junca de Almeida", publicPlaceNumber="411",
                                 publicPlace="Av Cantidio Sampaio" )

    def test_school_creation(self):
        self.assertTrue(self.scholl, School)
        self.assertEquals(self.scholl.__str__(), self.scholl.schoolName)


class TestLocation(TestCase):

    def setUp(self):
        self.location = mommy.make(Location, cityName="São Paulo", uf="SP")

    def test_location_creation(self):
        self.assertTrue(self.location, Location)
        self.assertEquals(self.location.__str__(), self.location.cityName)


class TestChildren(TestCase):

    def setUp(self):
        self.scholl = mommy.make(School, schoolName="Luiza Salete Junca de Almeida", publicPlaceNumber="411",
                                 publicPlace="Av Cantidio Sampaio")
        self.children = mommy.make(Children, name="Diego Delmiro", yearsOld="26", school=self.scholl)

    def test_Children_creation(self):
        self.assertTrue(self.children, Children)
        self.assertEquals(self.children.__str__(), self.children.name)


class TestParents(TestCase):

    def setUp(self):
        self.location = mommy.make(Location, cityName="São Paulo", uf="SP")
        self.scholl = mommy.make(School, schoolName="Luiza Salete Junca de Almeida", publicPlaceNumber="411",
                                 publicPlace="Av Cantidio Sampaio")
        self.children = mommy.make(Children, name="Diego Delmiro", yearsOld="26", school=self.scholl)
        self.parents = mommy.make(Parents, name="Jose Wilson", email="jwdalmieda@terra.com", numberPublicPlace="711",
                                  publicPlace="Rua nicia coutinho Patricio", contactNumberDDD="11",
                                  contactNumber="39831394", contactNumberMobiel="958044062", children=[self.children],
                                  location=self.location)

    def test_Parents_creation(self):
            self.assertTrue(self.parents, Parents)
            self.assertEquals(self.parents.__str__(), self.parents.name)