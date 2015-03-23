#!/usr/local/bin/python3 
#-*- coding:utf-8 -*-

"""
Resolution of problem 5 of project Euler

2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all 
of the numbers from 1 to 20?

"""

import sys

def no_remainder(total_divisible):
	n = 1
	while True:

		for i in range(1,total_divisible + 1):

			if(n % i) != 0:
				break
			
			if i == total_divisible:
				return n

		n += 1

if __name__ == "__main__":
	print(no_remainder(20))

	