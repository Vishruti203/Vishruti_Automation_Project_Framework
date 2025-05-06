# Creating two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Using union() - Combines elements from both sets (removes duplicates)
union_set = set1.union(set2)
print("Union:", union_set)  # Output: {1, 2, 3, 4, 5, 6}

# Using intersection() - Finds common elements between sets
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)  # Output: {3, 4}
