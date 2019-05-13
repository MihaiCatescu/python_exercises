# This exercise is for checking whether a number given by the user is prime or not.

# Solution 1 - Using functions

number = int(input("Give me a number: "))
numbers = list(range(1, number + 1))
divisors = []

def get_divisors(number):
    for i in numbers:
        if number % i == 0:
            divisors.append(i)
    return divisors

get_divisors(number)

def is_prime(number):
    if len(divisors) <= 2:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")

is_prime(number)

# Solution 2 -  without the use of functions
import sys
number = int(input("Insert a number" + "\n" + ">>> "))
prime = False

if number > 0:
    for i in range(2, number - 1):
        if number % i != 0:
            continue
        elif number % i == 0:
            sys.exit("The number is not prime.")
    sys.exit("The number is prime.")
elif number == 0:
    sys.exit("The number is not prime.")
else:
    sys.exit("The number is not prime.")