#!/usr/bin/python3.4
"""
https://projecteuler.net/problem=74

"""
import math


if __name__ == "__main__":

    counter = 0
    for x in range(1000000):
        # print("----")

        l = []
        l.append(x)
        y = x
        while True:
            s = sum([math.factorial(int(n)) for n in str(x)])
            if s in l:
                break
            else:
                l.append(s)
                x = s

        if len(l) == 60:
            # print(y, "->", l)
            counter = counter + 1
        del l

    print(counter)
