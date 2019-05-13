'''
This is function that takes a list and returns a new list that contains all the elements of the first list
minus all the duplicates.
'''

import random

# Solution 1

list_a = [random.randint(1, 20) for x in range(1, 11)] # Create a random 10 elements list with integers between 1 and 20
print(list_a)

def remove_duplicates(list_a):
    list_b = []
    for i in list_a:
        if i not in list_b:
            list_b.append(i)
    print(list_b)

remove_duplicates(list_a)

# Solution 2 - using sets

list_x = [random.randint(1, 20) for x in range(1, 11)]
print(list_x)
list_x = set(list_x)
print(list_x)
