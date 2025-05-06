def str_upper(func):
	def inner():
		str1 = func()
		return str1.upper()  
	return inner
  
def print_str():
	return "good morning"

print(print_str())

a = str_upper(print_str) # in python we use decorator instead of this.
print(a())


#===============================================================================
def str_upper1(func):
	def inner1():
		str2 = func()
		return str2.upper()
	return inner1 

@str_upper1()
def print_str1():
	return "good afternoon"
print(print_str1())

