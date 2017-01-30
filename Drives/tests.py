from django.test import TestCase
from model_mommy import mommy
from Clients.models import Location, Parents, School, Children
from .models import Driver, Vehicle


class TestDriver(TestCase):
    def setUp(self):
        self.location = mommy.make(Location, cityName="São Paulo", uf="SP")
        self.vehicle = mommy.make(Vehicle, vehicleType="Min Van", capacity=50)
        self.driver = mommy.make(Driver, name="Diego Delmiro", email="diego@gmail.com", contactNumberDDD="11",
                                 contactNumber="39831394", contactNumberMobile="958044062", categoryHab="D",
                                 location=self.location, vehicle=[self.vehicle])

    def test_Driver_creation(self):
        self.assertTrue(self.driver, Driver)
        self.assertEquals(self.driver.__str__(), self.driver.name)


class TestVehicle(TestCase):

    def setUp(self):

        self.location = mommy.make(Location, cityName="São Paulo", uf="SP")

        self.scholl = mommy.make(School, schoolName="Luiza Salete Junca de Almeida", publicPlaceNumber="411",
                                 publicPlace="Av Cantidio Sampaio")
        self.children = mommy.make(Children, name="Diego Delmiro", yearsOld="26", school=self.scholl)

        self.parents = mommy.make(Parents, name="Jose Wilson", email="jwdalmieda@terra.com", numberPublicPlace="711",
                                  publicPlace="Rua nicia coutinho Patricio", contactNumberDDD="11",
                                  contactNumber="39831394", contactNumberMobiel="958044062", children=[self.children],
                                  location=self.location)

        self.vehicle = mommy.make(Vehicle, vehicleType="Min Van", capacity=50, parents=[self.parents])

    def test_Vehicle_creation(self):
        self.assertTrue(self.vehicle, Vehicle)
        self.assertEquals(self.vehicle.__str__(), self.vehicle.vehicleType)
