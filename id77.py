#!/usr/bin/python3.4
"""
It is possible to write ten as the sum of primes in exactly
five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over
five thousand different ways?

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

    x = 0
    while len(primes) < 100:
        x = x + 1
        if is_prime(x):
            primes.append(x)

    # this value was tested manually...
    total = 71

    counter = [0] * (total + 1)
    counter[0] = 1

    for x in primes:
        # print("prime", x)
        for n in range(x, len(counter)):
            # print("n", n)
            counter[n] = counter[n] + counter[n - x]


    print("Value", total, "with", counter[-1], "possible primes sums")



