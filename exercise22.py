'''
Task:
Your task is to write a function which returns the sum of following series up to nth term(parameter).

Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...

Rules:
1. You need to round the answer to 2 decimal places and return it as String.
2. If the given value is 0 then it should return 0.00
3. You will only be given Natural Numbers as arguments.

Examples:
SeriesSum(1) => 1 = "1.00"
SeriesSum(2) => 1 + 1/4 = "1.25"
SeriesSum(5) => 1 + 1/4 + 1/7 + 1/10 + 1/13 = "1.57"
'''

def series_sum(n):
    series = []
    denominator = 4
    if n == 0:
        return '%.2f' % n
    elif n == 1:
        return '%.2f' % n
    elif n > 1:
        series.append(1)
        while len(series) < n:
            series.append(1 / denominator)
            denominator += 3
        total = sum(series)
        return '%.2f' % total
