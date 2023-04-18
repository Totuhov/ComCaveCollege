from machine_class import Machine

class Plane(Machine):
    def __init__(self, speed):
        self.speed = speed

    def __str__(self):
        return f"Plane:({self.speed})"
    
    def fly(self, length):
        print("Plane flies for " + str(length) + " hours.")

    def repair(self):
        print("Plane gets repaired.")