#! /usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
Resolution of problem 15

Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

https://projecteuler.net/project/images/p015.gif

How many such routes are there through a 20×20 grid?
"""


import math


def find_routes(columns):
    maximum_steps = columns * 2
    permutations = math.factorial(maximum_steps)\
        / math.pow(math.factorial(columns), 2)
    return permutations

if __name__ == "__main__":
    # for each column/row there are two choices Right or Down
    # the maximum steps of the path is the number of columns/rows
    # multiplied by 2
    # it these path we can choose evenly a number of Rights and Downs
    #
    # for 20 columns/rows it implies a max of 20 * 2 steps in the path
    # the evenly combination of 20 rights and 20 lefts is found using
    # the following permutation:
    # n! / n1! * n2!
    # n = 40, n1 = 20, n2 = 20
    # 40! / 20! * 20! = answer
    #
    # for the math permutation fundamental:
    # http://www.intmath.com/counting-probability/3-permutations.php

    print(find_routes(20))
