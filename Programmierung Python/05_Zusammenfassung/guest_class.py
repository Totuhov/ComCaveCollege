from restaurant_class import Restaurant

class Guest:
    def __init__(self, name, money, restaurant):
        self.name = name
        self.money = money
        self.restaurant = restaurant

    def __str__(self):
        return f"Guest:({self.money})-({self.name})"
    
    def visitRestaurant(self, restaurant):
        if restaurant.getsVisited():
            print(self, " visits ", restaurant)
