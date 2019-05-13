'''
Create a function that checks if a given word is a palindrome!
Palindrome = a word, phrase, or sequence that reads the same backwards as forwards (e.g. madam)
'''
def check_palindrome(word):
    word = word.lower()
    palindrome = word[::-1]
    if word == palindrome:
        print("The", word, "is a palindrome!")
    else:
        print("The", word, "is not a palindrome!")

check_palindrome(input("Give me a word please: "))