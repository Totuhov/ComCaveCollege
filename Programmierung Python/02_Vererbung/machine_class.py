class Machine:
    def __init__(self, speed):
        self.speed = speed

    def build(self):
        print("Machine gets built.")
        print(self.__class__.__name__)