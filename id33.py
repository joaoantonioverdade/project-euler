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

if __name__ == "__main__":

    for first in range(10, 99):
        for second in range(10, 99):
            fstr = str(first)
            sstr = str(second)

            res = first / second

            if res < 1:

                for fidx, f in enumerate(fstr):
                    for sidx, s in enumerate(sstr):

                        if int(s) == 0:
                            continue

                        sres = int(f) / int(s)
                        if sres == res:
                            print(first, second, f, s, res, sres, fidx, sidx)
