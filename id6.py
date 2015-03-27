#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
Resolution of problem 6 of project Euler

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

"""


def difference(length):
    """
    I simplify the maths

    (a + b + n)^2 - (a^2 + b^2 + n^2) = result
    2(ab + an + bn) = result

    """

    counter = 1
    sum_natural = 0

    # do the matrix combinations of all the natural numbers till the length
    #   a b c d
    # a X ! ! !
    # b X X ! !
    # c X X X !
    # d X X X X
    #
    # 2(ab + ac + ad + bc + bd + cd) = 2 * sum(!)
    for n in range(1, length + 1):
        for m in range(counter + 1, length + 1):
            sum_natural += n * m

        counter += 1

    return 2 * sum_natural

if __name__ == "__main__":
    print(difference(100))
