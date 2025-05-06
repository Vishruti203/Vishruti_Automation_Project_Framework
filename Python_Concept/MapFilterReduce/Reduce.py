'''Use reduce() when you need to combine elements into a single value, like calculating a sum or product. 
Since reduce() is not built-in, you need to import it from functools'''


'''Use reduce() when: ✔ You need to combine all elements into one value (e.g., sum, product). 
✔ You want to avoid writing manual loops for aggregation.'''


from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120
