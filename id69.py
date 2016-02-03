#!/usr/bin/python3.4
import math
import sys
from functools import reduce

"""
https://projecteuler.net/problem=69

To determine if two numbers are relatively prime, you need to first factor each
number into its prime factors -> prime_factorization
"""


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


def prime_factorization(n, primes):
    """ Tries to factorize from the lowest prime to the highest """
    factors = [1]
    factor = n
    while reduce(lambda x, y: x*y, factors) != n:
        for f in primes:
            if factor % f == 0:
                factor = factor / f
                factors.append(f)
                break

            if f == primes[-1]:
                print("not enough primes in the list!!!")
                sys.exit()
    return factors


primes = [x for x in range(1, 200) if is_prime(x)]
dic = {}

if __name__ == "__main__":
    res = 1
    n = 0
    limit = 1000000
    while res * primes[n] < limit:
        res = res * primes[n]
        n = n + 1

    print(res, n, prime_factorization(res, primes))

