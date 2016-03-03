#!/usr/bin/python3.4
"""
https://projecteuler.net/problem=75


It turns out that 12 cm is the smallest length of wire that can be bent to form
 an integer sided right angle triangle in exactly one way, but there are many
 more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an
integer sided right angle triangle, and other lengths allow more than one
solution to be found; for example, using 120 cm it is possible to form exactly
three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000
can exactly one integer sided right angle triangle be formed?

"""

import math


def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t

    return a

if __name__ == "__main__":

    # # a^2 + b^2 = c^2
    # Euclid's formula
    # pair m and n with m > n
    # m and n are coprime
    # m - n is odd

    # a = k * (m^2 - n^2)
    # b = k * (2mn)
    # c = k * (m^2 + n^2)

    l = []
    limit = 1500000
    for i in range(limit + 1):
        l.append(0)

    total = int(math.sqrt(limit / 2))

    counter = 0

    for m in range(2, total):
        for n in range(1, m):

            # odd
            if (m - n) % 2 != 0:

                # coprime
                if gcd(n, m) == 1:

                    a = m ** 2 - n ** 2
                    b = 2 * m * n
                    c = m ** 2 + n ** 2
                    p = a + b + c

                    # k *
                    while p <= limit:

                        l[p] = l[p] + 1

                        if (l[p] == 1):
                            counter = counter + 1
                        if (l[p] == 2):
                            counter = counter - 1

                        p = p + a + b + c

    print(counter)
