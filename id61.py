#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are 
all figurate (polygonal) numbers and are generated by the following formulae:

Triangle        P 3,n = n(n+1)/2       1, 3, 6, 10, 15, ...
Square          P 4,n = n^2             1, 4, 9, 16, 25, ...
Pentagonal      P 5,n = n(3n−1)/2      1, 5, 12, 22, 35, ...
Hexagonal       P 6,n = n(2n−1)        1, 6, 15, 28, 45, ...
Heptagonal      P 7,n = n(5n−3)/2      1, 7, 18, 34, 55, ...
Octagonal       P 8,n = n(3n−2)        1, 8, 21, 40, 65, ...

The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three 
interesting properties.

The set is cyclic, in that the last two digits of each number is the first two 
digits of the next number (including the last number with the first).
Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and 
pentagonal (P5,44=2882), is represented by a different number in the set.
This is the only set of 4-digit numbers with this property.
Find the sum of the only ordered set of six cyclic 4-digit numbers for which 
each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and 
octagonal, is represented by a different number in the set.
"""



import math
import itertools
import sys

def triangles(n):
    return n * (n + 1) / 2

def is_triangle(n):
    tri = (math.sqrt(8 * n + 1) + 1) / 2

    if round(tri, 0) == tri:
        return int(tri)
    else:
        return 0

def is_square(n):
    sq = math.sqrt(n)
    # print("->", sq, round(sq, 0))

    if round(sq, 0) == sq:
        return int(sq)
    else:
        return 0

def is_pentagonal(n):
    pent = (math.sqrt(24 * n + 1) + 1) / 6

    if round(pent, 0) == pent:
        return int(pent)
    else:
        return 0

def is_hexagonal(n):
    hexa = (math.sqrt(8 * n + 1) + 1) / 4

    if round(hexa, 0) == hexa:
        return int(hexa)
    else:
        return 0

def is_heptagonal(n):
    hep = (math.sqrt(40 * n + 9) + 3) / 10

    if round(hep, 0) == hep:
        return int(hep)
    else:
        return 0

def is_octogonal(n):
    octo = (math.sqrt(3 * n + 1) + 1) / 3

    if round(octo, 0) == octo:
        return int(octo)
    else:
        return 0




if __name__ == "__main__":


    base_tri = set()
    base_squ = set()
    base_pent = set()
    base_hexa = set()
    base_hept = set()
    base_octo = set()

    for n in range(1000, 10000):
        if is_triangle(n):
            base_tri.add(n)
        if is_square(n):
            base_squ.add(n)
        if is_pentagonal(n):
            base_pent.add(n)
        if is_hexagonal(n):
            base_hexa.add(n)
        if is_heptagonal(n):
            base_hept.add(n)
        if is_octogonal(n):
            base_octo.add(n)

    bases = []
    bases.append(base_tri)
    bases.append(base_squ)
    bases.append(base_pent)
    bases.append(base_hexa)
    bases.append(base_hept)
    bases.append(base_octo)

    for perm in itertools.permutations([1, 2, 3, 4, 5, 6], 6):

        tri = bases[perm.index(1)]
        squ = bases[perm.index(2)]
        pent = bases[perm.index(3)]
        hexa = bases[perm.index(4)]
        hept = bases[perm.index(5)]
        octo = bases[perm.index(6)]

        for n3 in tri:
            for n4 in squ:
                if str(n3)[2:] == str(n4)[:2]:
                    for n5 in pent:
                        if str(n4)[2:] == str(n5)[:2]:
                            for n6 in hexa:
                                if str(n5)[2:] == str(n6)[:2]:
                                    for n7 in hept:
                                        if str(n6)[2:] == str(n7)[:2]:
                                            for n8 in octo:
                                                if str(n7)[2:] == str(n8)[:2]:
                                                    if(str(n8)[2:] == str(n3)[:2]):
                                                        print(n3, n4, n5, n6, n7, n8)
                                                        print(n3 + n4 + n5 + n6 + n7 + n8)
                                                        sys.exit()

      

