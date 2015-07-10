#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt, a 15K text file
containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible
to try every route to solve this problem, as there are 299 altogether!
If you could check one trillion (1012) routes every second it would take over
twenty billion years to check them all.
There is an efficient algorithm to solve it. ;o)
"""


if __name__ == "__main__":

    with open('triangle.txt', 'r') as file_object:
        read_data = file_object.read()

    numbers = []
    for line in read_data.split("\n"):
        if line is not "":
            numbers.append(line)

    # first value
    ref_count = int(numbers[0])
    ref_id = 0
    numbers.pop(0)

    for idx, line in enumerate(numbers):

        all_actual_options = [int(num) for num in numbers[idx].split(" ")]
        actual_options = all_actual_options[ref_id:ref_id + 2]

        # find max from last line
        if len(numbers) <= idx + 1:
            ref_count += max(actual_options)
            break

        all_next_options = [int(num) for num in numbers[idx + 1].split(" ")]

        next_options = all_next_options[ref_id:]

        # print()
        # print("Actual Options", actual_options)
        # print("Next Options", next_options[:4])

        max_option = 0
        ref_temp = 0
        for idx_option, option in enumerate(actual_options):

            left_num = next_options[idx_option]
            right_num = next_options[idx_option + 1]

            if option + right_num > max_option:
                max_option = option + right_num
                ref_temp = idx_option

            if option + left_num > max_option:
                max_option = option + left_num
                ref_temp = idx_option

        ref_id += ref_temp
        ref_count += all_actual_options[ref_id]

        print("Ref", all_actual_options[ref_id], ref_count)
    print("Sum", ref_count)
