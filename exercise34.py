# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.


def double_char(s):
    new_s = []
    for letter in list(s):
        new_s.append(letter + letter)
    return ''.join(new_s)


double_char("1234!_ ")
