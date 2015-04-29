# !/usr/bin/python3.4
# -*- coding: utf-8 -*-


"""
Solution to problem 26


A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

1/2 =   0.5
1/3 =   0.(3)
1/4 =   0.25
1/5 =   0.2
1/6 =   0.1(6)
1/7 =   0.(142857)
1/8 =   0.125
1/9 =   0.(1)
1/10    =   0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.

"""


import re


def long_division(number):

    counter = 0

    numerator = 1
    denominator = number
    remainder = []
    result = ""

    while True:

        if numerator < denominator:

            numerator *= 10

        r = numerator % denominator

        if r in remainder:
            break

        remainder.append(numerator % denominator)
        result += str(int(numerator/denominator))

        numerator = remainder[-1]
        counter += 1

        if remainder[-1] == 0:
            break

    return result


# https://en.wikipedia.org/wiki/Repeating_decimal
# https://en.wikipedia.org/wiki/Cyclic_number
if __name__ == "__main__":

    longest_recurring = 0
    recurring = re.compile(r'(\d+?)\1+')

    for n in range(2, 1000):
        cyclic = long_division(n)

        if(len(cyclic) > longest_recurring):
            print(n, len(cyclic))
            longest_recurring = len(cyclic)
