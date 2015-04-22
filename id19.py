# !/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
Resolution of problem 19


You are given the following information, but you may prefer to do some research
for yourself.

1 Jan 1900 was a Monday.

Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century
unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
"""


def count_sundays(start_year, end_year):
    """ Counts the sundays beetween two dates """

    days_week = ["sunday", "monday", "tuesday", "wednesday", "thursday",
                 "friday", "saturday"]

    months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months_days_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    leap_year = False
    counter = 0
    weekday = 0

    # starts on the given year since we know it starts on a monday
    for year in range(1900, end_year + 1):

        # check for leap year
        # adds extra day on february
        if year % 100 == 0:
            if year % 400 == 0:
                leap_year = True
        elif year % 4 == 0:
            leap_year = True

        if leap_year:
            md = months_days_leap
        else:
            md = months_days

        for month in md:
            for day in range(1, month + 1):
                weekday += 1

                if weekday >= 7:
                    weekday = 0

                # print(year, month, day, days_week[weekday])
                if day == 1 and days_week[weekday] == "sunday":
                    if year >= start_year:
                        counter += 1

        leap_year = False

    return counter

if __name__ == "__main__":
    print(count_sundays(1901, 2000))
