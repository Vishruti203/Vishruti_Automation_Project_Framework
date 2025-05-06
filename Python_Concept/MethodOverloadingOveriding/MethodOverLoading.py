class Example:
    def display(self, a = None, b = None):
        if a and b:
            print(f"Two arguments : {a},{b}")
        elif a :
            print(f"one argument : {a}")
        else:
            print("No arguments")

obj = Example()
print(obj.display())
print(obj.display(10))
print(obj.display(10,20))