'''
1. Order vs. Unordered
List: Maintains the order of elements.

Set: Unordered; elements may appear in a different order.
'''

my_list = [10, 20, 30, 40]
my_set = {10, 20, 30, 40}

print(my_list)  # Output: [10, 20, 30, 40]
print(my_set)   # Output: {10, 40, 20, 30} (Order may change)


'''
2. Duplicates Allowed vs. Unique Elements
List: Allows duplicate values.

Set: Only stores unique elements; duplicates are automatically removed.
'''

list_example = [1, 2, 2, 3, 4, 4, 5]
set_example = {1, 2, 2, 3, 4, 4, 5}

print(list_example)  # Output: [1, 2, 2, 3, 4, 4, 5]
print(set_example)   # Output: {1, 2, 3, 4, 5} (Duplicates removed)


'''
3. Indexing and Accessing Elements
List: Supports indexing and slicing.

Set: Does not support indexing.
'''

my_list = [10, 20, 30, 40]
print(my_list[2])  # Output: 30 (Can access elements by index)

my_set = {10, 20, 30, 40}
print(my_set[2])  # ❌ ERROR! (Sets do not support indexing)


'''
4. Performance (Speed)
List: Slower for membership checks (in operation).

Set: Faster for membership checks due to hashing.
'''

my_list = [1, 2, 3, 4, 5]
my_set = {1, 2, 3, 4, 5}

print(3 in my_list)  # Slower check
print(3 in my_set)   # Faster check







