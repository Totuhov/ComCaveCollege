class Restaurant:
    def __init__(self, name):
        self.name = name
        self.maxGuests = 10
        self.guests = 0

    def __str__(self):
        return f"Restaurant:({self.name}) - ({self.guests})"
    
    def getsVisited(self):
        if(self.guests >= self.maxGuests):
            print("Can't accept more guests")
            return False
        else:
            self.guests += 1
            return True