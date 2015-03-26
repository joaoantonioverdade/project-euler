#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
Resolution of problem 10 of project Euler

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""


import math
import timeit


def sieve_eratosthenes(maximum):
    """
    The basic idea behind this ancient method is that instead of looking for
    divisors d of n, we mark multiples of d as composites. Since every
    composite has a prime divisor, the marking of multpiples need only be done
    for primes
    """

    N = maximum
    prime = []
    crossed = []

    for n in range(2, N):
        if n not in crossed:
            prime.append(n)

            if n > math.sqrt(N):
                for p in range(n + 1, N):
                    if p not in crossed:
                        prime.append(p)

                return prime

            for m in range(2, N):
                mult = n * m
                if mult < N:
                    crossed.append(mult)


def primes(maximum):
    prime = []
    for n in range(maximum):
        if is_prime(n):
            prime.append(n)

    return prime


def is_prime(number):
    """
    A slow prime checker function
    """

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


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


def find_fastest():
    """
    Measure functions time of processing
    """

    wrapped = wrapper(primes, 2000000)
    wrapped2 = wrapper(sieve_eratosthenes, 2000000)

    print("-----Taking times-----")
    print("->First function:")
    print(timeit.timeit(wrapped, number=1))
    print("->Second function:")
    print(timeit.timeit(wrapped2, number=1))

if __name__ == "__main__":
    # find_fastest()

    max_prime = 2000000
    sum_primes = 0
    for n in range(max_prime):
        if is_prime(n):
            sum_primes += n
    print(sum_primes)
