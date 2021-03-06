#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt, a 15K text file
containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible
to try every route to solve this problem, as there are 299 altogether!
If you could check one trillion (1012) routes every second it would take over
twenty billion years to check them all.
There is an efficient algorithm to solve it. ;o)
"""


if __name__ == "__main__":

    with open('triangle.txt', 'r') as file_object:
        read_data = file_object.read()

    numbers = []
    for line in read_data.split("\n"):
        if line is not "":
            numbers.append([int(n) for n in line.split(" ")])

    while(len(numbers) > 1):

        first_line = numbers.pop()
        for idx, n in enumerate(numbers[-1]):
            numbers[-1][idx] += max(first_line[idx:idx+2])

    print(numbers)
