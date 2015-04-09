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

    if columns == 1:
        return 2

    return find_routes(columns - 1) + (math.pow(columns, 2) - math.pow(columns - 1, 2) - 1) * 2

if __name__ == "__main__":
    # (1x1)     1 square    -> 2 routes
    # (2x2)     4 squares   -> 2 + 2 + 2 - 2 routes (6)
    # (3x3)     9 squares   -> (20)
    # (4x4)     16 squares  -> (70)
    # (nxn)     m squares   -> (n-1 routes) + (n*n - n-1 * n-1 - 1) * 2
    for n in range(1, 4):
        print(n, "->", find_routes(n))
