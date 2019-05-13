'''
Function that checks whether a given number is inside a list of numbers.
'''

import random

list_a = [1, 2, 3, 5, 8, 9, 16, 20, 22, 26, 30, 34, 35, 38, 41, 47, 52, 67, 88, 93, 99]
number = random.randint(1, 100)


def check_number(list_a, number):
    if number in list_a:
        print("The number " + str(number) + " is in the list.")
    else:
        print("The number " + str(number) + " is not in the list.")


def check(list_a, number):
    if number in list_a:
        option = True
        print(option)
    else:
        option = False
        print(option)

check_number(list_a, number)
check(list_a, number)