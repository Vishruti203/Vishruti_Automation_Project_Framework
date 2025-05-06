
print("===================================== Iterator ===============================================")
#Using tuple
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

print("=======================================================================================")

#using list
myList = [1,2,3]
iterator = iter(myList)
print(next(iterator))  #output:1
print(next(iterator))  #output:2

mylist =[1,2,3]
iterator = iter(mylist)

print(next(iterator))
print(next(iterator))
print(next(iterator))

print("===================================== Generator ===============================================")

def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2