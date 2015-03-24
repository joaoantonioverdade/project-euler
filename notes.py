#!/usr/bin/python3.4
#-*- coding: utf-8 -*-

""" 
Leftovers from the projects resolutions, to take a deeper look

"""

def combination(values,first=False,final=[]):
	"""
	Returns a list with all possible combinations of items in list 'values'

	It returns with duplicates, it must be a faster/cleaner way of doing it
	"""

	if len(values) > 0:
		
		final.append(values)
		combination(values[1:],final=final)
				
		for n in range(1,len(values)):
			new_values = copy.deepcopy(values)
			new_values.pop(n)
			combination(new_values,final=final)

	if first:
		return final

