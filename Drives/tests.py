from django.test import TestCase
from model_mommy import mommy
from Clients.models import Location
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
        self.vehicle = mommy.make(Vehicle, vehicleType="Min Van", capacity=50)

    def test_Vehicle_creation(self):
        self.assertTrue(self.vehicle, Vehicle)
        self.assertEquals(self.vehicle.__str__(), self.vehicle.vehicleType)