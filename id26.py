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

# https://en.wikipedia.org/wiki/Repeating_decimal
# https://en.wikipedia.org/wiki/Cyclic_number
if __name__ == "__main__":

    longest_recurring = 0
    recurring = re.compile(r'(\d+?)\1+')

    for d in range(2, 1000):
        value = str(1 / d)[2:]

        result = recurring.search(value)
        if result:
            if value.count(result.group(1)) >= longest_recurring:
                longest_recurring = value.count(result.group(1))
            print(d, value, result.groups(), len(result.group(1)), value.count(result.group(1)) )

    print(longest_recurring)
