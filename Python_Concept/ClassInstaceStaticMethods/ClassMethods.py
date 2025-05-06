''' Class methods can access and modify data that is shared across all 
 objects of the class—attributes defined directly within the class rather
 than specific to any one object.'''


class Example:
    shared_value = 100  # Class-level data

    @classmethod
    def class_method(cls):
        cls.shared_value += 10  # Modifying class-level data
        return cls.shared_value
print(Example.class_method())  # Outputs: 110


print("=============================================================================")

class Parent:
    shared_value = 100

    @classmethod
    def class_method(cls):
        return cls.shared_value

class Child(Parent):
    shared_value = 200

print(Parent.class_method())  # Outputs: 100
print(Child.class_method())   # Outputs: 200

