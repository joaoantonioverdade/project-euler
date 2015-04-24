# !/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
Resolution of problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


def d(number):
    "Sum of proper divisors of n"
    return sum([n for n in range(1, number) if number % n == 0])


def amicable_number(number):
    a = number
    b = d(a)
    c = d(b)

    if a == c and a != b:
        return True
    else:
        return False


if __name__ == "__main__":

    sum_amicables = 0

    for n in range(1, 10000):
        if amicable_number(n):
            sum_amicables += n

    print(sum_amicables)
