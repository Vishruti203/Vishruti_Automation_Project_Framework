'''From 2lists findout the missing item from 2nd list by comparing the first list.'''

# Define the two lists
list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 5]

# Find missing items
missing_items = [item for item in list1 if item not in list2]

# Output the result
print("Missing items from list2:", missing_items)

print("===================================== or ===================================")

list1 = [1,2,3,4,5]
list2 = [2,3,5]
list3 = []


for item in list1:
    if item not in list2:
        list3.append(item)
print(list3)
        


