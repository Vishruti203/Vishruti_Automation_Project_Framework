'''The super keyword in python is used to call methods from a parent class with in a child class.
Its particulary useful in inheritance when you want to extend the functionality of a parent class with out
completely overiding its method'''


class parent:
    def show(self):
        print("This is a parent method")

class child(parent):
    def show(self):
        super().show()
        print("This is a child method")

obj = child()
print(obj.show())
