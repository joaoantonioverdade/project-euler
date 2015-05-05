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


# Brute force takes ages...
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

        if sum(p * m for p, m in zip(pence, comb)) == find_pence:
            counter += 1

    # plus the 200 pences coin
    print(counter + 1)


pence = [200, 100, 50, 20, 10, 5, 2, 1]


# much faster
def recursion_pounds_to_pence(money, max_coin):
    coin_sum = 0
    if max_coin == 7:
        return 1

    for i in range(max_coin, 8):
        if (money - pence[i] == 0):
            coin_sum += 1
        if (money - pence[i] > 0):
            coin_sum += recursion_pounds_to_pence(money - pence[i], i)

    return coin_sum

if __name__ == "__main__":
    # pounds_to_pence(2)
    print(recursion_pounds_to_pence(5*100, 0))
