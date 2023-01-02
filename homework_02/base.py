from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight=1500, fuel=50, fuel_consumption=10, started=False):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("low fuel")

    def move(self, distance):
        if self.fuel >= self.fuel_consumption * distance:
            self.fuel -= distance * self.fuel_consumption
        else:
            raise NotEnoughFuel("not enough fuel")
