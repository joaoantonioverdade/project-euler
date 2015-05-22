#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""


import math

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
    primes = []

    max_prime = 1000000
    for n in range(1, max_prime + 1):
        if is_prime(n):
            primes.append(n)

    max_consecutive = 0
    max_found = 0
    for n in range(0, len(primes) + 1):

        # print("n", n)

        consecutive = 0
        length = 1
        while consecutive < max_prime and n + length <= len(primes):
            consecutive = sum(primes[n:n + length])

            if len(primes[n:n + length]) > max_consecutive and \
               consecutive in primes:

                max_consecutive = len(primes[n:n + length])
                max_found = consecutive

            length += 1

    print("Max", max_found, max_consecutive)
