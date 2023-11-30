import unittest
from car import Car
from motorcycle import Motorcycle
from vehicle import Vehicle


class VehicleTest(unittest.TestCase):
    def setUp(self):
        self.car = Car("Dodge", "Ram", 2023)
        self.motorcycle = Motorcycle("Honda", "CBR500R", 2022)

    def testCarIsInstanceOfVehicle(self):
        self.assertIsInstance(self.car, Vehicle)

    def testMotorcycleIsInstanceOfVehicle(self):
        self.assertIsInstance(self.motorcycle, Vehicle)

    def testCarHasFourWheels(self):
            self.assertEqual(self.car.numWheels, 4)

    def testMotorcycleHasTwoWheels(self):
            self.assertEqual(self.motorcycle.numWheels, 2)

    def testCarSpeedDuringTestDrive(self):
        self.car.testDrive()
        self.assertEqual(self.car.speed, 60)

    def testMotorcycleSpeedDuringTestDrive(self):
        self.motorcycle.testDrive()
        self.assertEqual(self.motorcycle.speed, 75)

    def testCarStopsDuringParking(self):
        self.car.testDrive()
        self.car.park()
        self.assertEqual(self.car.speed, 0)

    def testMotorcycleStopsDuringParking(self):
        self.motorcycle.testDrive()
        self.motorcycle.park()
        self.assertEqual(self.motorcycle.speed, 0)


if __name__ == '__main__':
        unittest.main()