''' Static method in python is a method inside the class that does not requires access to 
instance or class attributes. It is defined using @staticmethod and can be called without
instantiating the class '''


class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

# Calling the static method directly using the class name
print(MathOperations.add(10, 5))  # Output: 15

# Creating an instance and calling the static method
obj = MathOperations()
print(obj.add(10, 5))  # Output: 15
