#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
Resolution of problem 7 of project Euler

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10 001st prime number?

"""


import math


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


if __name__ == "__main__":

    find_prime = 10001
    counter = 0
    count_prime = 0

    # Runs the iteration until the nTH number (find_prime)
    while count_prime < find_prime:
        if is_prime(counter):
            count_prime += 1

        if count_prime == find_prime:
            print(counter)

        counter += 1
