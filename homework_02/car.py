"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    def __init__(self, weight=1500, fuel=50, fuel_consumption=10, started=False):
        super().__init__(weight, fuel, fuel_consumption, started)
        self.engine = None

    def set_engine(self, engine: Engine):
        self.engine = engine

