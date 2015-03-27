#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
Resolution of problem 3 of project Euler

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

import copy


def is_prime(number):
    """
    A slow prime checker function
    """

    # only valid for numbers > 2
    for n in range(2, number - 1):
        if number % n == 0:
            return False

    return True


# reference http://www.mathsisfun.com/prime-factorization.html
def prime_factorization(number, primes, factors=[]):
    """ Tries to factorize from the lowest prime to the highest """

    mod = number % primes[0]

    if(mod == 0):
        factors.append(primes[0])
        result = number / primes[0]
        prime_factorization(result, primes, factors)

    else:
        new_primes = copy.deepcopy(primes)
        new_primes.pop(0)
        if len(new_primes) > 0:
            prime_factorization(number, new_primes, factors)

    return factors


if __name__ == "__main__":

    number = 600851475143
    try_maximum = 7000

    primes = []

    for n in range(2, try_maximum):
        if is_prime(n):
            primes.append(n)

    print(prime_factorization(number, primes, []))
