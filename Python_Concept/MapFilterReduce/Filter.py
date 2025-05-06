'''Use filter() when you need to extract elements from a list based on a condition.'''

'''Use filter() when: ✔ You need to keep only the elements that satisfy a condition. 
✔ You want a more readable way to perform selection without loops.'''

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6]
