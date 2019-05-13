'''
This is a program that ask the user for a level of security and generates a password.
'''
import random
import string

levels = str(["weak", "medium", "strong", "titan"])
weak_pass = ["sausage", "123456", "password", "street", "kitty", "morning", "monkey", "station", "electric"]

print("This is a password generator! The level of security for the passwords are: " + levels)

answer = input("Please choose the level of security you want for your password: ").lower()

while answer not in levels:
    answer = input("Please choose a valid level of security: ")


def generate_pass(string_length=6):
    password = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password) for i in range(string_length))


if answer == "weak":
    print("Your password is: " + random.choice(weak_pass))
elif answer == "medium":
    print("Your password is: " + generate_pass(6))
elif answer == "strong":
    print("Your password is: " + generate_pass(12))
elif answer == "titan":
    print("Your password is: " + generate_pass(17))