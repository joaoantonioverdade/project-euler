# !/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
Solution to problem 27

Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values
n = 0 to 39.
However, when n = 40, 40² + 40 + 41 = 40(40 + 1) + 41 is divisible by 41,
and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80
primes for the consecutive values n = 0 to 79.
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n = 0.
"""


import math


def is_prime(number):
    """
    A slow prime checker function
    """

    number = abs(number)

    if number == 1:
        return False

    # For faster processment
    # All primes except 2 are odd
    if number % 2 == 0 and number != 2:
        return False

    if number % 3 == 0 and number != 3:
        return False

    # Only up to the square root
    for n in range(2, math.trunc(math.sqrt(number)) + 1):
        if number % n == 0:
            return False

    return True


def quadratic(n, a, b):
    return (n * n) + (a * n) + b


if __name__ == "__main__":

    # brute force
    max_primes = 0
    coefficients = None
    for a in range(-999, 1000):
        for b in range(-999, 1000):

            n = 0
            while True:
                if is_prime(quadratic(n, a, b)) is True:

                    n += 1

                    if n > max_primes:
                        max_primes = n
                        coefficients = [a, b]
                else:
                    break

    print(max_primes, coefficients, coefficients[0] * coefficients[1])
