#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
The cube, 41063625 (345^3), can be permuted to produce two other
cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 
is the smallest cube which has exactly three permutations of 
its digits which are also cube.

Find the smallest cube for which exactly five permutations of 
its digits are cube.
"""


import math
import sys


if __name__ == "__main__":
    cubes = []
    total_cubes = 10000

    for n in range(1, total_cubes):
        cubes.append(sorted(str(n ** 3)))

    for n in cubes:
        if cubes.count(n) >= 5:
            for m in range(1, total_cubes):
                if sorted(str(m ** 3)) == n:
                    print(m ** 3)
                    sys.exit()
