'''
Ask the user for a number. Depending on whether the number is even or odd, print out an
appropriate message to the user.

Extras:

1.If the number is a multiple of 4, print out a different message.
2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''

#Extra 1
num = int(input("Please give me a number: "))
if num % 4 == 0:
    print(num, "is a multiple of 4!")
elif num % 2 == 0:
    print(num, "is an even number. ")
else:
    print(num, "is an odd number.")

#Extra 2
check = int(input("Please give me a second number: "))
if num % check == 0:
    print(check, "divides evenly in", num)
else:
    print(check, "does not divide evenly in", num)