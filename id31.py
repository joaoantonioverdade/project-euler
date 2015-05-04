#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
Solution to problem 31

In England the currency is made up of pound, £, and pence, p, and there are
eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""


import itertools


def pounds_to_pence(pounds):

    find_pence = pounds * 100
    pence = [1, 2, 5, 10, 20, 50, 100]
    max_range = [find_pence,
                 find_pence // 2,
                 find_pence // 5,
                 find_pence // 10,
                 find_pence // 20,
                 find_pence // 50,
                 find_pence // 100]

    hypothesis_range = []
    for e in max_range:
        hypothesis_range.append(list(range(0, e + 1)))

    counter = 0
    for comb in itertools.product(*hypothesis_range):

        # print(comb)
        if sum(p * m for p, m in zip(pence, comb)) == find_pence:
            counter += 1

    # plus the 200 pences coin
    print(counter + 1)

if __name__ == "__main__":
    pounds_to_pence(2)
