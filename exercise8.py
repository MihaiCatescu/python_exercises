import random

number = random.randint(1, 9)
guess = 0
count = 0

while guess != number and guess != "exit":
    guess = input("Please give me a number between 1 and 9: \n")

    if guess == "exit":
        break

    guess = int(guess)
    count += 1

    if guess < number:
        print("-----------------------------------------\n"
              "Your number is smaller than the one I am looking for. Try again.\n"
              "Try again or enter 'exit' to exit.\n"
              "-----------------------------------------")
    elif guess > number:
        print("-----------------------------------------\n"
              "Your number is greater than the one I am looking for. Try again.\n"
              "Try again or enter 'exit' to exit.\n"
              "-----------------------------------------")
    else:
        print("-----------------------------------------\n"
              "That is the number I am looking for. Thank you!\n"
              "It only took you", count, "tries.\n"
              "-----------------------------------------")
        break
