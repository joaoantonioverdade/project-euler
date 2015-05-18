#!/usr/bin/python3.4
# -*- coding: utf-8 -*-


"""
The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below one million?
"""

import math
import itertools
import sys


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

    primes = set()
    not_circular = set()
    for n in range(1, 1000000):

        if n in not_circular:
            continue

        if is_prime(n) is True:

            if n not in primes:

                circular = True

                n_str = str(n)

                perms = []
                for p in itertools.permutations(n_str, len(n_str)):

                    p_str = ''.join(p)
                    if p_str[0] != "0":
                        perms.append(p_str)

                temp_primes = []
                for p in perms:

                    if int(p) not in temp_primes:
                        temp_primes.append(int(p))

                    if is_prime(int(p)) is False:
                        circular = False

                for t in temp_primes:
                    if circular is True:
                        primes.add(t)

                    else:
                        not_circular.add(t)

    print(primes)
    print("Total", len(primes))
