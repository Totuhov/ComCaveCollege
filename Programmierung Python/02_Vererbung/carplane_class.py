from car_class import Car
from plane_class import Plane

class Carplane(Plane, Car):
    def __init__(self, speed):
        self.speed = speed

    def __str__(self):
        return f"Carplane:({self.speed})"
    