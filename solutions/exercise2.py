def geometric_series(a0, r, n):
    sum = a0
    term = a0
    for i in range(n):
        term *= r
        sum += term
    return sum


def is_divisible(numerator, denominator):
    if numerator % denominator == 0:
        return True
    return False


def smallest_divisible(numerator):
    if (numerator < 2):
        return -1
    for i in range(2, round(numerator/2), 1):
        if is_divisible(numerator, i):
            return i
    return numerator


def is_prime(number):
    if (smallest_divisible(number) == number):
        return True
    return False


def is_leapyear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
