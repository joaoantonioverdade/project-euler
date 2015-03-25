#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
"""
Resolution of problem 9 of project Euler

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""


def brute():
    sum_naturals = 1000
    maximum_natural = 600
    for a in range(1, maximum_natural):
        for b in range(a + 1, maximum_natural):
            for c in range(b + 1, maximum_natural):
                if(a+b+c == sum_naturals):
                    if (a*a+b*b == c*c):
                        print(str(a) + "+" + str(b) + "+" + str(c) + " = " +
                              str(a*b*c))

if __name__ == "__main__":
    brute()
