#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the
maximum digital sum?
"""


if __name__ == "__main__":

    max_sum = 0

    for a in range(1, 101):
        for b in range(1, 101):

            resulting_sum = sum([int(n) for n in str(a ** b)])
            if resulting_sum > max_sum:
                max_sum = resulting_sum

    print(max_sum)
