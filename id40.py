#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
An irrational decimal fraction is created by concatenating the positive
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the
following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""


if __name__ == "__main__":

    d = 0
    counter = 1
    parts = set()
    while d < 1000000:

        for c in str(counter):
            d += 1

            # print(counter, d, c)

            if d in [1, 10, 100, 1000, 10000, 100000, 1000000]:
                parts.add(int(c))

        counter += 1

    print(parts)

    mult = 1
    for p in parts:
        mult *= p

    print(mult)
