# Write a function that rearranges an integer into its largest possible value.
# Note: If the argument passed through is single digit or is already the maximum possible integer, your function should
# simply return it.


def super_size(num):
    num = list(str(num))
    num.sort(reverse=True)
    return int(''.join(num))


super_size(69)
