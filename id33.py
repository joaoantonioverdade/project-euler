#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
Solution to problem 33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.

"""


# note: one should remove a COMMON digit in both the nominator and the
# denominator.
# Brute force again...
if __name__ == "__main__":

    for first in range(10, 99):
        for second in range(10, 99):
            fstr = str(first)
            sstr = str(second)

            res = first / second

            if res < 1:

                fidx = list(fstr[:])
                sidx = list(sstr[:])

                for f in fidx:
                    if f in sidx:

                        if f == '0':
                            continue

                        fidx.remove(f)
                        sidx.remove(f)

                        if int(''.join(sidx[:])) == 0:
                            continue

                        sres = int(''.join(fidx)) / int(''.join(sidx[:]))
                        if sres == res:
                            print(first, second, fidx, sidx, res, sres)

#  0.25 * 0.2 * 0.4 * 0.5 = 0.01 = 1/100 (nom/denom) denom = 100
