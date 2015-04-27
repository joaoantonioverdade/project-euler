# !/usr/bin/python3.4
# -*- coding: utf:8 -*-

"""
    Solution to problem 25

    The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
    Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144
    The 12th term, F12, is the first term to contain three digits.

    What is the index of the first term in the Fibonacci sequence to contain
    1000 digits?

"""


def find_fib():

    values = [1, 1]

    counter = 1

    while True:

        temp = values[0] + values[1]
        values[0] = values[1]
        values[1] = temp

        counter += 1

        if(len(str(values[0])) >= 1000):
            print("Index", counter)
            break


if __name__ == "__main__":
    find_fib()
