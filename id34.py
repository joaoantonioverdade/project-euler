#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

import math


if __name__ == "__main__":

    fact = []

    for n in range(0, 10):
        fact.append(math.factorial(n))

    print([n for n in range(0, 10)])
    print(fact)


    for n in range(3, 10000000):

        nstr = str(n)

        sum_fact = 0
        for c in nstr:
            sum_fact += fact[int(c)]

        if n == sum_fact:
            print(n, sum_fact)

    # 3
    # 3 in fact? no

    pass
