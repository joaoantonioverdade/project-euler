#!/usr/bin/python3.4
"""
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two
positive integers?

"""


if __name__ == "__main__":

    total = 100
    counter = [0] * (total + 1)
    counter[0] = 1

    for n in range(1, total):
        for m in range(n, total + 1):
            counter[m] = counter[m] + counter[m - n]

    print(counter)
