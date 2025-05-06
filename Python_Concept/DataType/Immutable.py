'''Immutable datatypes in python are those that can not be chnaged onece they are created'''

#1)String

s = "hello"
s[0] = "H" #This will raise an error


#2)Tuple

t = (1,2,3)
t[0] = 10  #This wil raise an error

#3)Integer(int)

x= 5
x += 1  #new object is created, x is not modified in place.

#4)Frozen sets(forzenset) 

s = frozenset([1,2,3])
s.add(4) #Raise an error2


