#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
"""

import itertools
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

if __name__ == "__main__":

    base = "123456789"
    pandigital = set()
    largest = 0

    for n in range(len(base) + 1, 1, -1):

        for p in itertools.permutations(base[:n], n):
            number = int(''.join(p))

            if is_prime(number) and number > largest:
                largest = number

        if largest != 0:
            print(largest)
            break
