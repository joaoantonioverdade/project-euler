#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated
numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and
56993. Consequently 56003, being the first member of this family, is the
smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value
family.
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


def most_common(lst):
    return max(set(lst), key=lst.count)

if __name__ == "__main__":

    # primes = []
    primes = set()
    min_prime = 100000
    max_prime = 1000000

    max_count = 0
    find = 8
    for n in range(min_prime, max_prime):

        if is_prime(n):
            primes.add(str(n))

    base = range(0, len(str(max_prime)) - 1)

    for combinations in range(1, len(str(min_prime))):
        for c in itertools.combinations(base, combinations):
            index = [x for x in c]
            # print("Index", index)

            temp_primes = []
            for p in primes:

                tp = ""
                for idx, c in enumerate(p[:]):
                    if idx in index:
                        tp += "#"
                    else:
                        tp += c

                temp_primes.append(tp)

            for n in set(temp_primes):
                if temp_primes.count(n) >= find:

                    count_primes = 0
                    for x in range(0, 10):
                        if n.replace("#", str(x)) in primes:

                            if n.replace("#", str(x))[0] != "0":
                                count_primes += 1
                                # print("...", n.replace("#", str(x)))

                    if count_primes == find:

                        print(n)
                        print("Found")
                        sys.exit()
