#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
The 5-digit number, 16807=7^5, is also a fifth power. 
Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""


if __name__ == "__main__":

    counter = 0
    for k in range(1, 100):
        for n in range(1, 50):
            if len(str(n ** k)) == k:
                counter += 1
        
    print(counter)
