#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
and concatenating them in any order the result will always be prime.
For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these
four primes, 792, represents the lowest sum for a set of four primes with this
property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
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
    prime_pairs = set()
    primes_comb = set()

    max_try = 10000
    max_comb = 5

    for n in range(1, max_try):
        if is_prime(n):
            primes.add(n)

    for combs in range(2, max_comb + 1):

        print("#", combs)
        sys.stdout.flush()

        if combs == 2:
            for perm in itertools.combinations(primes, combs):
                primes_comb.add(perm)
        else:
            new_primes = set()
            for p in primes_comb:
                for n in primes:
                    if n > p[-1]:
                        if n not in p:
                            new_primes.add(p + (n,))

            primes_comb = new_primes

        new_primes = set()
        for perm in primes_comb:

            prime_concatenation = True
            for n in perm[:-1]:

                if is_prime(int(str(n) + str(perm[-1]))) is False or \
                   is_prime(int(str(perm[-1]) + str(n))) is False:
                    prime_concatenation = False
                    break

            if prime_concatenation is True:
                new_primes.add(perm)
                if combs == max_comb:
                    prime_pairs.add(sum(perm))
        primes_comb = new_primes

    if(len(prime_pairs) > 0):
        print("Prime pairs set sum:", prime_pairs, min(prime_pairs))
