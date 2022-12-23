from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight = 1500
    started = False
    fuel = 50
    fuel_consumption = 10

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("low fuel")

    def move(self, distance):
        if self.fuel > 0 and self.fuel_consumption > 0 and self.fuel >= self.fuel_consumption * distance:
            self.fuel -= distance * self.fuel_consumption
        else:
            raise NotEnoughFuel("not enough fuel")
