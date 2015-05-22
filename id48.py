#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""


if __name__ == "__main__":

    series_sum = 0
    for n in range(1, 1001):

        # print("#", n)

        unity_place = n
        for i in range(1, n):

            unity_place *= n

            if unity_place >= 1000000000:
                unity_place = int(str(unity_place)[-10:])

        series_sum += unity_place
        if series_sum >= 1000000000:
                series_sum = int(str(series_sum)[-10:])

    print(series_sum)
