#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

"""
Resolution of problem 4 of project Euler

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit
numbers.

"""

import math


def number_places(n):
    """
    Really ugly extraction of unity cases to a list
    """

    bases = []
    while n >= 10:

        n = n / 10

        bases.append(int(round(n-int(math.trunc(n)), 1) * 10))

        n = int(math.trunc(n))

        if n < 10:
            bases.append(n)

    return list(reversed(bases))


def check_palindrome(number):
    places = number_places(number)

    # check for palindrome
    palindrome = True
    for i in range(math.trunc(len(places) / 2)):

        # can also be done using the reverse number and doing a
        # comparison
        left = i
        right = len(places) - i - 1
        if(places[left] != places[right]):
            palindrome = False

    return palindrome


def largest_palindrome(min, max):

    max += 1

    highest_palindrome = 0
    # for each two 3-digit number product
    for left_number in reversed(range(min, max)):
        for right_number in reversed(range(min, max)):

            product = left_number * right_number

            # palindrome = check_palindrome(product)
            # palindrome = (reverse(product) == product)
            palindrome = (reverse2(product) == product)

            if palindrome:
                if(highest_palindrome < product):
                    highest_palindrome = product

    return highest_palindrome


def reverse(num):
    rev = 0
    while(num > 0):

        rev = (10 * rev) + num % 10

        # floor division
        num = num // 10

    return rev


def reverse2(num):
    return int(str(num)[::-1])

if __name__ == "__main__":
    print(largest_palindrome(100, 999))
