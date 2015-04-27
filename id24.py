#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
Resolution of problem 24

A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

import itertools


# TODO: implement own permutation
def combination(digits, position):
    perm = list(itertools.permutations(digits))
    print(perm[position - 1])


if __name__ == "__main__":
    combination([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1000000)
