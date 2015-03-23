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
	n = total_divisible[0]
	while True:

		for i in total_divisible: 

			if(n % i) != 0:
				break

			if i == total_divisible[-1]:
				return n

		n += 20
		
if __name__ == "__main__":
	print(no_remainder([20,19,18,17,16,15,14,13,12,11]))

#20 10 5
#19 8 4 2 1
#18 9 3 
#17
#16 8
#15 5
#14 7
#13
#12 6 3 
#11
