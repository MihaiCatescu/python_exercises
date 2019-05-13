'''
This is a program that asks the user for a long string containing multiple words and prints back to the user
the same string, except with the words in backwards order.
'''

phrase = input("Please write a sentence: ")

def reverse_phrase(phrase):
    phrase = phrase.split()
    phrase = phrase[::-1]
    phrase = " ".join(phrase)
    print(phrase)

reverse_phrase(phrase)

# Short solution

def reverse(phrase):
    print(" ".join(phrase.split()[::-1]))
reverse(phrase)