#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""


def angles(perimeter):

    solutions = 0

    # print("#", perimeter)

    for a in range(1, perimeter):
        for b in range(a, perimeter):

            c = perimeter - a - b
            if a * a + b * b == c * c:
                # print(a, b, c)
                solutions += 1

    return solutions

if __name__ == "__main__":

    max_p = 0
    max_solutions = 0
    for n in range(1, 1000):
        ang = angles(n)
        if ang > max_solutions:
            max_solutions = ang
            max_p = n

    print(max_p)
