'''
Mr. Scrooge has a sum of money 'P' that wants to invest, and he wants to know how many years 'Y' this sum has to be
kept in the bank in order for this sum of money to amount to 'D'.
The sum is kept for 'Y' years in the bank where interest 'I' is paid yearly, and the new sum is re-invested yearly
after paying tax 'T'.
Note that the principal is not taxed but only the year's accrued interest.
Thus Mr. Scrooge has to wait for 3 years for the initial pricipal to amount to the desired sum.
Your task is to complete the method provided and return the number of years 'Y' as a whole in order for Mr. Scrooge to
get the desired sum.
Assumptions : Assume that Desired Principal 'D' is always greater than the initial principal, however it is best to
take into consideration that if the Desired Principal 'D' is equal to Principal 'P' this should return 0 Years.
'''


def calculate_years(principal, interest, tax, desired):
    years = 0
    while principal < desired:
        principal = float((principal * interest) - ((principal * interest) * tax) + principal)
        years += 1
    return years


calculate_years(1000, 0.05, 0.18, 1100)
