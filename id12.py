#!/usr/bin/python3.4
# -*- coding:utf-8 -*-

"""
Resolution of problem 12

The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ..

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred
divisors?
"""
import math
import sys


def brute(maximum, divisors):
    oc = []
    factors_result = []

    for n in range(1, maximum + 1):

        if n % 2 == 0 and n != 2:
            continue

        if n % 3 == 0 and n != 3:
            continue

        if n % 5 == 0 and n != 5:
            continue

        if n % 7 == 0 and n != 7:
            continue

        if n % 11 == 0 and n != 11:
            continue



        for m in range(1, maximum + 1):
            factors_result.append((n * m))

    counter_triangle = 0
    for n in range(1, maximum + 1):
        counter_triangle = counter_triangle + n

        oc.append(factors_result.count(counter_triangle))

        if factors_result.count(counter_triangle) == divisors:
            print("Found number with", divisors, "divisors:", counter_triangle)
            return

    print("No number found with", divisors, "divisors, max ocurrences:",
          max(oc))


def brute2(divisors):

    actual_divisor = 0
    counter_triangle = 0
    max_divisors = 0

    n = 0
    while actual_divisor < divisors:
        n = n + 1
        counter_triangle = counter_triangle + n
        triangle_divisors = []
        counter_divisors = 1
        for d in range(1, math.trunc(counter_triangle // 2) + 1):
            if counter_triangle % d == 0:
                counter_divisors = counter_divisors + 1
                # triangle_divisors.append(d)

        # triangle_divisors.append(counter_triangle)
        # actual_divisor = len(triangle_divisors)
        actual_divisor = counter_divisors

        if counter_divisors > max_divisors:
            max_divisors = counter_divisors
            print("->", counter_triangle, "#", counter_divisors)
            # print(triangle_divisors)
            sys.stdout.flush()

        if counter_triangle % 10000 == 0:
            print(counter_triangle,"...")

if __name__ == "__main__":
    # brute(1500, 50)
    # brute2(500)
