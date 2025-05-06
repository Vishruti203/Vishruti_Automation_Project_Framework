'''A method that operates on the class itself rather that on an instance.
Instance methods use the self keyword, which represents a specific object (or "instance") 
created from a class. This lets instance methods access and modify data (attributes) that 
belong only to that particular object. '''


'''Instance methods (self): Deal with attributes specific to 
individual objects (instances) of the class.'''

class Example:
    def instance_method(self):
        self.value = 10  # Modifying instance-specific data
        return self.value
obj1 = Example()
print(obj1.instance_method())  # Outputs: 10
