from animal_class import Animal # Importieren von Code aus anderen Dateien.
from cat_class import Cat
from persian_class import Persian

dog = Animal(5, 15, "female")
print(dog.getAge())
dog.makeSound()
Animal.makeSound()
dog.__age = 10
print(dog.__age)
Animal.__age = 5

garfield = Cat(2, 5, "male", "red")
print(garfield.getAge())
print(garfield.gender)
print(garfield.color)

felix = Persian(4, 4, "female", "green")
print(felix.getAge())

print("-----")
print(dog)
print("-----")