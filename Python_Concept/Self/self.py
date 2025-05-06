class example:
    def set_data(self,data):
        self.data = data

    def get_data(self, data):
        return self.data
    

obj1 = example()
obj2 = example()

obj1.set_data(10)
obj2.set_data(20)


print(obj1.get_data(10))  # Output: 10
print(obj2.get_data(20))  # Output: 20
