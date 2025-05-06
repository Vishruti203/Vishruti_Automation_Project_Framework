class Animal:
    def make_sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def make_sound(self):  # Overriding the parent method
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

# Using polymorphism
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.make_sound())  # Calls the overridden method
