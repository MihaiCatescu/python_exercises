'''
The goal of this exercise is to convert a string to a new string where each character in the new string is "("
if that character appears only once in the original string, or ")" if that character appears more than once
in the original string. Ignore capitalization when determining if a character is a duplicate.
'''

from collections import Counter

def duplicate_encode(word):
    word = word.lower()
    new_string = ''
    count = Counter(word)
    for letter in word:
        if count[letter] == 1:
            new_string += '('
        else:
            new_string += ')'
    return new_string

print(duplicate_encode(input("Enter a word: ")))
