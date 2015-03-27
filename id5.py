#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

"""
Resolution of problem 5 of project Euler

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?

"""


def no_remainder(total_divisible):
    n = total_divisible[0]
    while True:

        for i in total_divisible:

            if(n % i) != 0:
                break

            if i == total_divisible[-1]:
                return n

        # We can increment by the largest multiple saving us time
        n += 20

if __name__ == "__main__":
    # If its divisible by 20 its by 10 and 5 also
    # If its divisible by 18 its by 9
    # If its divisible by 16 its bu 8 and 4 and 2 ...
    print(no_remainder([20, 19, 18, 17, 16, 15, 14, 13, 12, 11]))
