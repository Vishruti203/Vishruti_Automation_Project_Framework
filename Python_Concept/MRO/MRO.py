class A:
    def show(self):
        print("Method from class A")
class B(A):
    pass

class C(A):
    def show(self):
        print("Method from class C")

class D(B,C):
    pass

obj = D()
print(obj.show())
print("===================================================")
print(D.mro())

