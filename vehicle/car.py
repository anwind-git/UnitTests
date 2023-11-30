from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, company, model, year):
        super().__init__(company, model, year)
        self.numWheels = 4
        self.speed = 0

    def testDrive(self):
        self.speed = 60

    def park(self):
        self.speed = 0

    def __str__(self):
        return f"Этот автомобиль {self.yearRelease} года выпуска, производитель {self.company}, модель {self.model}"