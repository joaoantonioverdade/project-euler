#!/usr/bin/python3.4

"""
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""


import itertools


def pandigital_product():

    # brute force
    possible_numbers = "123456789*="
    products = []

    for permutation in itertools.permutations(possible_numbers):

        if permutation.index('=') < permutation.index('*'):
            continue

        if permutation.index('=') == len(permutation) - 1:
            continue

        if permutation.index('=') == 0 or permutation.index('*') == 0:
            continue

        if permutation.index("*") == permutation.index("=") - 1:
            continue

        first = int(''.join(permutation[0:permutation.index('*')]))
        second = int(''.join(permutation[permutation.index('*') + 1:permutation.index('=')]))
        result = int(''.join(permutation[permutation.index('=') + 1:]))

        if first * second == result:
            if result not in products:
                print(''.join(permutation))
                products.append(result)

    print("Sum", sum(products))

if __name__ == "__main__":
    pandigital_product()