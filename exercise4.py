'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
'''

num = int(input("Please insert a number: "))
nums = list(range(1, num + 1))
divisors = []
for elem in nums:
    if num % elem == 0:
        divisors.append(elem)
    else:
        continue

print("The divisors of", num, "are:", ", ".join(repr(e) for e in divisors))

