#!/usr/bin/python3.4

# BRUTEFORCE
import sys
import itertools

if __name__ == "__main__":
	keys = []
	with open('p079_keylog.txt') as file:
		keys = [line.rstrip() for line in file]

	for r in range(3,9):
		solutions = itertools.product("0123456789", repeat=r)

		for i in solutions:
			sol = ''.join(i) 
			found = True
			for key in keys:
				index = -1

				for k in key:
					if k not in sol:
						index = -1
						break

					sindex = sol.index(k)
					if sindex > index:
						index = sindex
					else:
						index = -1
						break
				if index == -1:
					found = False
					break

			if found:
				print "KEY FOUND", sol
				sys.exit()
