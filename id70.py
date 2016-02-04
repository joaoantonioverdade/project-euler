#!/usr/bin/python3.4
import math
import sys
import itertools
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


primes = [x for x in range(1, 10000) if is_prime(x)]
dic = {}

if __name__ == "__main__":

    # values between 1597 and 3167
    # square_root(10^7) ~ 3162
    print(primes[300:450])
    min_n = 0
    min_v = 99

    for idx, x in enumerate(primes[300:500]):
        print("#", idx)
        sys.stdout.flush()
        for y in primes[300:550]:
            n = x * y

            if n > math.pow(10, 7):
                continue

            comb = []
            for i in itertools.permutations(str(n)):
                if i[0] != '0':
                    comb.append(int(''.join(i)))

            pf = prime_factorization(n, primes)
            parcels = [(1-1/j) for j in set(pf[1:])]
            res = int(reduce(lambda x, y: x*y, parcels) * n)

            # # print(res)
            if res in set(comb):
                print(n, x, y, res, n/res)

                if n/res < min_v:
                    min_v = n / res
                    min_n = n


    print("finished", min_n, min_v)
