#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
Starting with 1 and spiralling anticlockwise in the following way, a square
spiral with side length 7 is formed.

37! 36  35  34  33  32  31!
38  17! 16  15  14  13! 30
39  18   5!  4   3! 12  29
40  19   6   1   2  11  28
41  20   7!  8   9  10  27
42  21  22  23  24  25  26
43! 44  45  46  47  48  49

It is interesting to note that the odd squares lie along the bottom right
diagonal, but what is more interesting is that 8 out of the 13 numbers lying
along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral
with side length 9 will be formed. If this process is continued, what is the
side length of the square spiral for which the ratio of primes along both
diagonals first falls below 10%?
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

    diag = 1
    cumo = 2
    layer = 1
    primes = set()

    while True:

        for n in range(1, 5):
            diag += cumo

            if(is_prime(diag)):
                primes.add(diag)

        print("Ratio", len(primes) / (1 + layer * 4))

        if len(primes) / (1 + layer * 4) < 0.1:
            print("side length", 1 + layer * 2)
            break

        cumo += 2
        layer += 1
