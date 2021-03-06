#! /usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
Resolution of problem 23

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
number.

A number n is called deficient if the sum of its proper divisors is less
than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers
is less than this limit.

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.

"""


def sum_proper_divisors_slow(number):
    "Sum of proper divisors of n"
    return sum([n for n in range(1, number) if number % n == 0])


def sum_proper_divisors(number):
    "Sum of proper divisors of n"
    return sum([n for n in range(1, number // 2 + 1) if number % n == 0])


if __name__ == "__main__":

    abundant = set()
    total = 28124

    for number in range(1, total):
        if sum_proper_divisors(number) > number:
            abundant.add(number)

    abundant_sorted = sorted(abundant)
    count_sum = 0

    for number in range(1, total):

        print(number)

        in_ab = False
        for ab in abundant_sorted:

            if ab > number // 2:
                break

            if (number - ab) in abundant_sorted:
                in_ab = True
                break

        if in_ab is False:
            count_sum += number

    print(count_sum)
