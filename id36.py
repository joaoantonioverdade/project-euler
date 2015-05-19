#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""


def palindromic(number):

    s_number = str(number)
    if s_number == s_number[::-1]:
        return True


if __name__ == "__main__":

    palindromic_dec_bin = set()
    for n in range(1, 1000000):
        if palindromic(n) and palindromic(format(n, 'b')):
            palindromic_dec_bin.add(n)

    print(palindromic_dec_bin)
    print(sum(palindromic_dec_bin))
