#!/usr/bin/python3.4

import itertools


def bruteforce():

    # movimentos
    l = (len(matrix) - 1) * 2

    min_cost = 0
    ways = 0
    for n in itertools.product("RD", repeat=l):
        if n.count("R") == n.count("D"):
            ways += 1

            # calculate cost
            idx, idy = 0, 0
            cost = 0

            cost = matrix[idx][idy]

            for m in n:
                if m == "R":
                    idx += 1
                if m == "D":
                    idy += 1

                cost += matrix[idx][idy]

            if min_cost == 0 or min_cost > cost:
                min_cost = cost

    print("minimum cost of {}".format(min_cost))


def search():

    for x in range(len(matrix)):
        for y in range(len(matrix)):

            left_cell = None
            top_cell = None

            if x > 0:
                left_cell = matrix[x - 1][y]
            if y > 0:
                top_cell = matrix[x][y - 1]

            # print(left_cell, top_cell)
            if not (x == 0 and y == 0):
                if left_cell is None:
                    matrix[x][y] += top_cell
                elif top_cell is None:
                    matrix[x][y] += left_cell
                else:
                    matrix[x][y] += min(left_cell, top_cell)

    print("minimum cost of {}".format(matrix[-1][-1]))


if __name__ == "__main__":

    # more precision due to rounding
    matrix = []
    with open("p081_matrix.txt", "r") as file_object:
        lines = file_object.readlines()

    for line in lines:
        row = [int(n.rstrip()) for n in line.split(',')]
        matrix.append(row)

    #bruteforce()
    search()