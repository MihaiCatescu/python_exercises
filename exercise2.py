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