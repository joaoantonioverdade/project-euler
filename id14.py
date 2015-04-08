#! /usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
Resolution of problem 14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def collatz_chain(maximum):

    max_chain = 0
    max_number = 0

    for n in range(1, maximum + 1):

        chain = n
        count_chain = 1

        while chain != 1:

            if chain % 2 == 0:
                chain = chain / 2
            else:
                chain = (3 * chain) + 1

            count_chain += 1

        if count_chain > max_chain:
            max_chain = count_chain
            max_number = n

    return (max_number, max_chain)


if __name__ == "__main__":
    print(collatz_chain(1000000))
