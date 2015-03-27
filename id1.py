#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
Resolution of problem 1 of project Euler

If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

NOTE: 0 is always a multiple, although the euler project ommited it
"""

import timeit


def multiples(number, maximum):
    """
    Returns all the multiples of the given 'number' to a certain maximum
    """

    return [n for n in range(1, maximum) if n % number == 0]


def multiples2(number, maximum):
    """
    Expliciting using a mathematical thinking procedure

    In mathematics, a multiple is the product of any quantity and an integer.
    In other words, for the quantities a and b, we say that b is a multiple
    of a if b = na for some integer n, which is called the multiplier or
    coefficient.
    """

    multiples_list = []

    counter = 1
    while (counter * number) < maximum:
        multiples_list.append(counter * number)
        counter = counter + 1

    return multiples_list


# http://www.pythoncentral.io/time-a-python-function/
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


def find_fastest():
    """
    Measure functions time of processing
    """
    wrapped = wrapper(multiples, 3, 1000)
    wrapped2 = wrapper(multiples2, 3, 1000)

    print("-----Taking times-----")
    print("->First function:")
    print(timeit.timeit(wrapped, number=1000))
    print("->Second function:")
    print(timeit.timeit(wrapped2, number=1000))


if __name__ == "__main__":

    # find_fastest()
    list_multiples = set(multiples2(3, 1000) + multiples2(5, 1000))
    print(sum(list_multiples))

    # or one-liner:
    # print(sum(n for n in range(1,1000) if n % 3 == 0 or n % 5 == 0))
