#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5 C 3 = 10.

In general,

n C r = n! / r!(n−r)!
,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23 C 10 = 1144066.

How many, not necessarily distinct, values of  n C r, for 1 ≤ n ≤ 100, are
greater than one-million?
"""


import math


def total_combinations(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))

if __name__ == "__main__":

    counter = 0
    for n in range(1, 101):
        for r in range(1, n):
            if total_combinations(n, r) > 1000000:
                counter += 1

    print(counter)
