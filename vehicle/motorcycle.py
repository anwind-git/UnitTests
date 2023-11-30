from vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, company, model, year):
        super().__init__(company, model, year)
        self.numWheels = 2
        self.speed = 0

    def testDrive(self):
        self.speed = 75

    def park(self):
        self.speed = 0

    def __str__(self):
        return f"Этот мотоцикл {self.yearRelease} года выпуска, производитель {self.company}, модель {self.model}"