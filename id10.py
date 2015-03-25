#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
Resolution of problem 10 of project Euler

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""


import math


def is_prime(number):
    """
    A slow prime checker function
    """

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


if __name__ == "__main__":

    max_prime = 2000000
    sum_primes = 0
    for n in range(max_prime):
        if is_prime(n):
            sum_primes += n
    print(sum_primes)
