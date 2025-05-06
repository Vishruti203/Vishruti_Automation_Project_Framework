'''method overriding occurs when a child class redefines a method from the  parent class using then same name
and parameter .This supports polymorphism, allowing objects to behave dynamically'''



class parent:
    def show(self):
        print("parent class method")
class child(parent):
    def show(self):
        print("child class method")


obj = child()
print(obj.show()) #class overidden method from child class.


class a:
    def show(self):
        print("a")
class b(a):
    def show(self):
        print("b")

obj = b()
print(obj.show())