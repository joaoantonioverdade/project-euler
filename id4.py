#!/usr/local/bin/python3 
#-*- coding:utf-8 -*-

"""
Resolution of problem 4 of project Euler

A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit
numbers.

"""

import math
import sys

def number_places(n):
	
	# TODO: find a better way
	# really ugly extraction of unity cases
	bases = []
	while n >= 10:
				
		n = n / 10

		bases.append(int(round(n-int(math.trunc(n)),1) * 10))

		n = int(math.trunc(n))

		if n < 10 :
			bases.append(n)


	return list(reversed(bases))

def largest_palindrome(min,max):

	max += 1

	palindromes = []
	# for each two 3-digit number product
	for left_number in reversed(range(min,max)):
		for right_number in reversed(range(min,max)):
			
			product = left_number * right_number

			# get number with each numerical place in a list
			places = number_places(product)

			# check for palindrome
			palindrome = True 
			for i in range(math.trunc(len(places) / 2)):

				# TODO: there must be a better way
				left = i
				right = len(places) - i - 1
				if(places[left] != places[right]):
					palindrome = False

			if palindrome:
				print(str(left_number) + "*" + str(right_number) + "=" + str(product))
				palindromes.append(product)

	print(sorted(list(set(palindromes))))

if __name__ == "__main__":
	largest_palindrome(100,999)

