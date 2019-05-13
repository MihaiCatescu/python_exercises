'''
Create a function that takes a list of numbers and makes a new list of only the first and
last elements of the given list
'''

import random

list_a = random.sample(range(100), 10)

def new_list():
    list_b = []
    list_b.append([list_a[0], list_a[-1]])
    print(list_b)

new_list()