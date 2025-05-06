from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract Class
    @abstractmethod
    def make_sound(self):
        pass  # Must be implemented in subclasses

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

# Attempting to instantiate the abstract class will raise an error
# animal = Animal()  # ❌ ERROR: Abstract classes cannot be instantiated

dog = Dog()
cat = Cat()

print(dog.make_sound())  # Output: Bark
print(cat.make_sound())  # Output: Meow
