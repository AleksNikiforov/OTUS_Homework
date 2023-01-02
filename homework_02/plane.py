"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, weight):
        actual_cargo = self.cargo + weight
        if actual_cargo <= self.max_cargo:
            self.cargo = actual_cargo
        else:
            raise CargoOverload('Overload')

    def remove_all_cargo(self):
        cargo_now = self.cargo
        self.cargo = 0
        return cargo_now
