#!/usr/bin/python3.4

from decimal import *

if __name__ == "__main__":

    # more precision due to rounding
    getcontext().prec = 110

    total = 0
    for n in range(1, 100):
        v = Decimal(n).sqrt().as_tuple()[1]

        # racionais
        if len(v) == 1:
            continue

        total = total + sum(v[:100])

    print(total)
