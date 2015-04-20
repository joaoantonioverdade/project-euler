# !/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
Resolution of problem 17


If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.
"""

units = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
         'nine', '']
teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
         'seventeen', 'eighteen', 'nineteen']
tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
        'eighty', 'ninety']
thousands = ['hundred', 'thousand', 'million', 'billion', 'trillion']


def number2word(n):

    extendend = ""
    number_word = str(n)

    if n in range(11, 19 + 1):
        extendend = teens[n - 11]
    else:
        if len(number_word) >= 1:
            extendend = units[int(number_word[-1]) - 1]

        if len(number_word) >= 2:
            extendend = tens[int(number_word[-2]) - 1] + " " + extendend

        if len(number_word) >= 3:
            _tens = n - (int(number_word[-3]) * 100)

            extendend = units[int(number_word[-3]) - 1] + " " + \
                       thousands[len(number_word) - 3]

            if n % 100 != 0:
                extendend += " and " + number2word(_tens)

    return extendend


if __name__ == "__main__":

    count_chars = 0
    for n in range(1, 1001):
        print(n, number2word(n))
        count_chars += len(number2word(n).replace(" ", ""))

    # ugly hack (plus the 'one' from one thousand)
    print(count_chars + 3)
