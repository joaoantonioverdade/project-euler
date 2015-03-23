#!/usr/bin/python3.4
#-*- coding: utf-8 -*-

"""
Resolution of problem 3 of project Euler

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?


WORK IN PROGRESS....
"""

import math

def highest_prime_factor(number):

	find = number - 1

	# while (number % find != 0) and not is_prime(find):
	while (number % find != 0) and not trial_division(find):

		find -= 1

	return find


def is_prime(number):
	"""

	So slow that it is not feasible

	"""

	
	# only valid for numbers > 2
	for n in range(2,number - 1):
		if number % n == 0:
			return False  

	return True


import sys
import copy

def matrix(values,first=False,final=[]):

	

	if len(values) > 0:
		
		final.append(values)
		matrix(values[1:],final=final)
				
		for n in range(1,len(values)):
			new_values = copy.deepcopy(values)
			new_values.pop(n)
			matrix(new_values,final=final)

	if first:
		return final

# TODO clean
# reference http://www.mathsisfun.com/prime-factorization.html
def prime_factorization(number,primes):

	mod = number % primes[0]

	if(mod == 0):
		print(primes[0])
		result = number / primes[0]
		prime_factorization(result,primes)
	else:
		new_primes = copy.deepcopy(primes)
		new_primes.pop(0)
		if len(new_primes) > 0:
			prime_factorization(number,new_primes)


if __name__  == "__main__":	  
	
	number = 600851475143
	primes = []

	#for n in range(2,math.ceil(math.sqrt(600851475142))):
	for n in range(2,7000):
		if is_prime(n):
			primes.append(n)


	print(primes)
	sys.stdout.flush()
	
	prime_factorization(number,primes)

	sys.exit()

	number = 600851475143
	primes = []

	for n in range(2,32):
		
		if is_prime(n):
			primes.append(n)


	unique_combination = []
	for combination in matrix(primes,True):
		if combination not in unique_combination:
			unique_combination.append(combination)

	print(unique_combination)

	for c in unique_combination:
		mult = 1
		for n in c:
			mult *= n

		if mult == number:
			print("!!!!!!!!!!")
			print(c)
			sys.exit()

		else:
			print("-----")
			print(c)
			print(mult)

			sys.stdout.flush()




