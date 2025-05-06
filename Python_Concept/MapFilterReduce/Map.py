'''Use map() when you need to apply a function to each element in a sequence and return a transformed list.'''

'''💡 Use map() when: ✔ You need to modify each element in a list. 
✔ You want to apply a function to all items efficiently.'''


temps_celsius = [0, 10, 20, 30]
temps_fahrenheit = list(map(lambda c: (c * 9/5) + 32, temps_celsius))
print(temps_fahrenheit)  # Output: [32.0, 50.0, 68.0, 86.0]
