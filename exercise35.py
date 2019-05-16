'''
Create a function with two arguments that will return a list of length (n) with multiples of (x).
Assume both the given number and the number of times to count will be positive numbers greater than 0.
'''


def count_by(x, n):
    multiples = []
    y = x
    while len(multiples) < n:
        multiples.append(x)
        x += y
    return multiples
    # Short Version: return [i * x for i in range(1, n + 1)]


count_by(1, 10)
