# Your task is simply to count the total number of lowercase letters in a string.
# Extra 1: Write a function that counts the total number of uppercase letters in a string


def lowercase_counter(strng):
    counter = 0
    for i in strng:
        if i.islower():
            counter += 1
    print(counter)
    return counter


def uppercase_counter(strng):
    counter = 0
    for i in strng:
        if i.isupper():
            counter += 1
    print(counter)
    return counter


lowercase_counter("alknsgbkUDJNNDPfsdg")
uppercase_counter("alknsgbkUDJNNDPfsdg")