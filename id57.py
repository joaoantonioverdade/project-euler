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


if __name__ == "__main__":

    actual_numerator = 1
    actual_denominator = 1

    last_numerator = 1
    last_denominator = 1

    numerator_exceeds = 0

    for n in range(1, 1001):

        actual_numerator = 2 * last_denominator + last_numerator
        actual_denominator = last_denominator + last_numerator

        # print("#", n)
        # print(actual_numerator, "/", actual_denominator)
        # print(last_numerator, "/", last_denominator)

        last_numerator = actual_numerator
        last_denominator = actual_denominator

        if len(str(actual_numerator)) > len(str(last_denominator)):
            numerator_exceeds += 1

    print("Numerator exceeds", numerator_exceeds)
