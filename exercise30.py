'''
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
'''

import string

scores = dict()
for index, letter in enumerate(string.ascii_lowercase):
    scores[letter] = index + 1


def high(x):
    highest_word = ""
    highest_score = 0
    words = x.split(" ")
    print(words)

    for word in words:
        cur_score = score(word)
        if cur_score > highest_score:
            highest_score = cur_score
            highest_word = word
    return highest_word


def score(word):
    score = 0

    for x in range(0, len(word)):
        if word[x].isalpha():
            score += scores[word[x].lower()]
    return score


high("asasc asawf assa")
