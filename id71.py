#!/usr/bin/python3.4
"""
https://projecteuler.net/problem=71

n / d
if n < d and HCF(n,d)=1 it is called a reduced proper fraction
"""

if __name__ == "__main__":

    # p / q < n / d
    # p < (n * q) / d

    pivot = 3 / 7
    closest = 1
    min_value = pivot + 1
    max_q = 1000000
    for q in range(2, max_q):
        p = int((3 * q) / 7)

        res = pivot - p / q
        if res > 0 and res < closest:
            closest = res
            values = (p, q, res)

    print(values)
