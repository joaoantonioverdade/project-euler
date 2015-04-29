# !/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
Solution to problem 28

Starting with the number 1 and moving to the right in a clockwise direction a
5 by 5 spiral is formed as follows:

(21)  22  23  24 (25)
 20  (7)  8  (9)  10
 19   6  (1)  2   11
 18  (5)  4  (3)  12
(17)  16  15  14 (13)

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
in the same way?
"""


def diagonal(base, multiple, columns):
    n = 1
    c = 1
    result = 0
    while c <= columns:

        # print(base, n, base * n)
        result += base * n

        n += 1 + multiple * c
        c += 1

    # adds the columns because the its assuming n, n+1 from the center...
    return result + columns


def ediagonal(base, multiple, columns):
    """
    Can't figure out the relation in any other way...
    """

    n = 1
    c = 1
    result = 0
    while c <= columns:

        # print(base, n, base * n + (2 * c))
        result += base * n + (2 * c)

        n += 1 + multiple * c
        c += 1

    # adds the columns because the its assuming n, n+1 from the center...
    return result + columns
if __name__ == "__main__":
    """
    There is a relation in the diagonal numbers that is explored.
    With a spiral starting at n, and adding n+1 in each iteration,
    each column has a relation with its base value and its multiples
    except the left top column which I just couldn't figure it out
    so used the bottom right as relation.
    """

    total = 1
    # 500 + 500 + 1 = 1001
    columns = 500
    total += diagonal(8, 1, columns)
    total += diagonal(2, 4, columns)
    total += diagonal(4, 2, columns)
    total += ediagonal(4, 2, columns)

    print(total)
