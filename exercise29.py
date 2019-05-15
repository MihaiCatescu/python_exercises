'''
Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built
with the sides of given length and false in any other case.
'''


def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
    # return (a < b + c) and (b < a + c) and (c < a + b) -> single line solution


is_triangle(2, 4, 6)
