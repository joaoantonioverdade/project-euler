#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes
"""

import math
import itertools


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

    truncatable_prime = set()
    find_prime = True

    counter = 10
    while len(truncatable_prime) < 11:

        str_counter = str(counter)

        if is_prime(counter):

            fit = True
            for i in range(1, len(str_counter)):

                if not (is_prime(int(str_counter[i:])) and
                   is_prime(int(str_counter[:i]))):

                    fit = False
                    break

            if fit:
                truncatable_prime.add(counter)

        counter += 1

    print(truncatable_prime)
    print(sum(truncatable_prime))
