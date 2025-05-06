def str_upper(func):
	str1 = func()
	return str1.upper()
    
def print_str():
	return "Good morning"

print(print_str())

a = str_upper(print_str)
print(a)