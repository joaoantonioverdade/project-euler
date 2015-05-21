#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors.
What is the first of these numbers?
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

primes = set()


def trial_division_slow(n):

    dividers = []
    for c in range(1, n + 1):

        if c in primes:
            if n % c == 0:

                dividers.append(c)

    return dividers

def trial_division_set(n):

    dividers = []

    for c in primes:
        if n % c == 0:
            dividers.append(c)

    return dividers


primes_list = []
def trial_division(n):

    dividers = []

    for c in primes_list:
        if n % c == 0:
            dividers.append(c)

        if c > n:
            break

    return dividers


if __name__ == "__main__":

    max_prime = 1000000

    for n in range(1, max_prime):
        if is_prime(n):
            primes.add(n)
            primes_list.append(n)

    print(primes)

    last_row = 0
    seq = []

    for n in range(100000, max_prime):

        td = trial_division(n)
        if len(td) > 1:

            print("#", n, td)
            sys.stdout.flush()

            if last_row == n - 1:

                seq.append(n - 1)
                find_seq = 4

                if len(set(td)) < find_seq or \
                   len(set(trial_division(n - 1))) < find_seq:
                    seq.clear()

                elif len(seq) == find_seq - 1:
                    print(n, seq, td)
                    sys.exit()

            else:
                seq.clear()

            last_row = n
