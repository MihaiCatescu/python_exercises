'''
Write a function that returns the century of a given year.
'''

def centuryFromYear(year):
    century = year / 100
    century = str(century)
    decimal = int(century[-1:])
    if len(str(year)) <= 3:
        integer = int(str(century)[:1])
    else:
        integer = int(str(century)[:2])

    if decimal > 0:
        return integer + 1
    else:
        return integer

print(centuryFromYear(8))