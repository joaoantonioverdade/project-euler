#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
"""


if __name__ == "__main__":

    n = 1
    find = True
    while find:

        print(n)

        s = str(n)

        if set(s) == set(str(n * 2)) and \
           set(s) == set(str(n * 3)) and \
           set(s) == set(str(n * 4)) and \
           set(s) == set(str(n * 5)) and \
           set(s) == set(str(n * 6)):

            find = False

        n += 1
