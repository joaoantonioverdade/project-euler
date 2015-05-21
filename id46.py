#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?
"""


import math
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

    counter = 2
    search = True
    primes = set()

    while search:

        p = False
        if is_prime(counter):
            p = True
            primes.add(counter)

        if counter % 2 != 0 and p is False:
            print(counter)
            sys.stdout.flush()

            check_composite = False

            for prime in primes:
                res = 1
                while prime + (2 * math.pow(res, 2)) <= counter:

                    if prime + (2 * math.pow(res, 2)) == counter:
                        check_composite = True

                    res += 1

            if check_composite is False:
                sys.exit()
                break


        counter += 1
