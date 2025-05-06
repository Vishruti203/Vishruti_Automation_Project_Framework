
print("=====================================Example of private ====================================")
class MyClass:
    def __init__(self):
        self.__privateVar = 42  # Private variable

    def __privateMethod(self):
        print("This is a private method")

obj = MyClass()

# Trying to access private members directly
print(obj.__privateVar)  # ❌ ERROR: Attribute not accessible
obj.__privateMethod()    # ❌ ERROR: Method not accessible

# Using name mangling to access private members
print(obj._MyClass__privateVar)  # ✅ Works: Output -> 42
obj._MyClass__privateMethod()    # ✅ Works: Output -> "This is a private method"

print("=====================================Example of protected ====================================")
class Parent:
    def __init__(self):
        self._protectedVar = "Protected Value"

class Child(Parent):
    def show(self):
        print(self._protectedVar)  # ✅ Accessible in subclass

obj = Child()
obj.show()  # Output -> "Protected Value"

# Direct access (not recommended, but possible)
print(obj._protectedVar)  # ✅ Works, but should be avoided
