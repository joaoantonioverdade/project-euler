#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
It is possible to show that the square root of two can be expressed as an
infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth
expansion, 1393/985, is the first example where the number of digits in the
numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator
with more digits than denominator?
"""


import fractions


# too much recursion for python...
def get_expansion(n, expansion):

    if n == 1:
        return 1 / 2
    else:
        expansion = 1 / (2 + get_expansion(n - 1, expansion))

    return expansion


def first_try():

    larger_numerator = 0
    for n in range(1, 4):

        expansion = 1 + get_expansion(n, 1)
        res = fractions.Fraction(expansion).limit_denominator()

        if len(str(res.numerator)) > len(str(res.denominator)):
            larger_numerator += 1

        print(n, expansion, res.numerator, res.denominator)

    print(larger_numerator)


if __name__ == "__main__":
    pass