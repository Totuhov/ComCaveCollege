from machine_class import Machine

class Car(Machine):
    def __init__(self, speed):
        self.speed = speed

    def __str__(self):
        return f"Car:({self.speed})"
    
    def drive(self, length):
        print("Car drives for " + str(length) + " miles.")

    def repair(self):
        print("Car gets repaired.")