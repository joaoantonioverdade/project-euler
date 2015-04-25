#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
Resolution of problem 22

Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order.

Then working out the alphabetical value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?


"""

if __name__ == "__main__":

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                'Y', 'Z']

    with open('names.txt', 'r') as file_object:
        read_data = file_object.read()

    names = []

    for name in read_data.split(","):
        names.append(name[1:-1])

    names.sort()

    total_names_score = 0
    for name in names:
        name_score = 0
        for letter in name:
            name_score += alphabet.index(letter) + 1

        total_names_score += (name_score * (names.index(name) + 1))

    print(total_names_score)
