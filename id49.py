#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
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


def possible_solution():
    primes = set()
    for n in range(1000, 10000):
        if is_prime(n):
            primes.add(str(n))

    for prime in primes:

        permutations = set()
        for perm in itertools.permutations(prime, 4):

            perm_value = ''.join(perm)
            if perm_value != prime and perm_value in primes:
                permutations.add(perm_value)

        if str(int(prime) + 3330) in permutations and \
           str(int(prime) + 6660) in permutations:
            print("permutations", permutations)
            print(prime, int(prime) + 3330, int(prime) + 6660)

if __name__ == "__main__":

    for n in range(1000, 10000):
        first = is_prime(n)
        second = is_prime(n + 3330)
        third = is_prime(n + 6660)

        if first and second and third:
            if set(str(n)) == set(str(n + 3330)) and \
               set(str(n)) == set(str(n + 6660)):
                # & set(str(n + 6660)):
                print(n, n + 3330, n + 6660)
