#! /usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
Resolution of problem 16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


import math


def brute(n):
    soma = sum([int(x) for x in str(int(math.pow(2, n)))])
    print(soma)


if __name__ == "__main__":
    brute(1000)
