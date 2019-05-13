'''
This is a program that asks the user how many Fibonacci numbers to generate and then generates them.
'''

number = int(input("How many numbers of the Fibonacci sequence would you like me to display: "))
fibonacci_list = [1, 1]

def create_fibonacci(number):
    if number <= 2:
        len(fibonacci_list) == number
        print(fibonacci_list[0:number])
    else:
        while len(fibonacci_list) <= number:
            fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
        print(fibonacci_list)

create_fibonacci(number)