#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so
the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value
is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle
words?
"""


def seq_triangle(n):
    return 0.5 * n * (n + 1)


if __name__ == "__main__":

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                'Y', 'Z']

    triangle_words = []
    triangle_values = set()
    max_n = 0
    counter_n = 0

    with open('words.txt', 'r') as file_object:
        read_data = file_object.read()

    words = []
    for word in read_data.split(","):
        sum_word = sum([alphabet.index(c) + 1 for c in word[1: -1]])

        while max_n < sum_word:
            max_n = seq_triangle(counter_n)
            triangle_values.add(max_n)
            counter_n += 1

        if sum_word in triangle_values:
            triangle_words.append(word[1: -1])

        # print(word[1: -1], sum_word, triangle_words)

    print(len(triangle_words))
