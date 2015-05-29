#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest
value wins; for example, a pair of eights beats a pair of fives
(see example 1 below). But if two ranks tie, for example, both players have a
pair of queens, then highest cards in each hand are compared
(see example 4 below); if the highest cards tie then the next highest cards
are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You
can assume that all hands are valid (no invalid characters or repeated cards),
each player's hand is in no specific order, and in each hand there is a clear
winner.

How many hands does Player 1 win?
"""


order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


def is_royal_flush(cards):
    if 'T' in cards and \
       'J' in cards and \
       'Q' in cards and \
       'K' in cards and \
       'A' in cards:
        return True


def high(cards):
    values = [s[0] for s in cards.split(' ')]

    for idx, v in enumerate(values):
        if v == 'T':
            values[idx] = 10
        if v == 'J':
            values[idx] = 11
        if v == 'Q':
            values[idx] = 12
        if v == 'K':
            values[idx] = 13
        if v == 'A':
            values[idx] = 14

        values[idx] = int(values[idx])

    # print(sorted(values))
    return sorted(values)[-1]


def is_straight(cards):
    return is_all_consecutives(cards)


def is_straight_flush(cards):

    if is_same_suit(cards) and is_all_consecutives(cards):
        return True
    else:
        return False


def is_same_suit(cards):
    suit = [s[1] for s in cards.split(' ')]

    if len(set(suit)) != 1:
        return False
    else:
        return True


def is_all_consecutives(cards):

    values = [s[0] for s in cards.split(' ')]

    for idx, v in enumerate(values):
        if v == 'T':
            values[idx] = 10
        if v == 'J':
            values[idx] = 11
        if v == 'Q':
            values[idx] = 12
        if v == 'K':
            values[idx] = 13
        if v == 'A':
            values[idx] = 14

        values[idx] = int(values[idx])

    last = 0
    for v in sorted(values):
        if v == last + 1 or last == 0:
            last = v
            continue

        return False

    return True


def is_one_pair(cards):
    return has_pair(cards)


def is_two_pair(cards):
    values = ''.join([s[0] for s in cards.split(' ')])

    count_pairs = 0
    for v in values:
        if values.count(v) == 2:
            count_pairs += 1

    if count_pairs == 4:
        return True

    return False


def is_three_kind(cards):
    if max_kind(cards) == 3:
        return True
    else:
        return False


def is_four_kind(cards):
    if max_kind(cards) == 4:
        return True
    else:
        return False


def is_full_house(cards):
    if max_kind(cards) == 3 and has_pair(cards):
        print(cards)
        return True

    else:
        return False


def is_flush(cards):
    return is_same_suit(cards)


def has_pair(cards):
    values = ''.join([s[0] for s in cards.split(' ')])

    for v in values:
        if values.count(v) == 2:
            return True

    return False

def which_pair(cards):
    values = ''.join([s[0] for s in cards.split(' ')])

    for v in values:
        if values.count(v) == 2:
            return v

    return False


def max_kind(cards):

    values = ''.join([s[0] for s in cards.split(' ')])

    max_kind = 0
    for v in values:
        if values.count(v) > max_kind:
            max_kind = values.count(v)

    return max_kind


if __name__ == "__main__":

    with open('poker.txt', 'r') as file_object:
        read_data = file_object.read()

    player1_victories = 0
    player2_victories = 0

    for sentence in read_data.split("\n"):

        print('')
        if sentence == "":
            break

        player1 = sentence[:14]
        player2 = sentence[15:]

        highest = 0

        if is_royal_flush(player1):
            highest = 10
        elif is_straight_flush(player1):
            highest = 9
        elif is_four_kind(player1):
            highest = 8
        elif is_full_house(player1):
            highest = 7
        elif is_flush(player1):
            highest = 6
        elif is_straight(player1):
            highest = 5
        elif is_three_kind(player1):
            highest = 4
        elif is_two_pair(player1):
            highest = 3
        elif is_one_pair(player1):
            highest = 2

        print(player1, highest)

        ph = highest

        highest = 0
        if is_royal_flush(player2):
            highest = 10
        elif is_straight_flush(player2):
            highest = 9
        elif is_four_kind(player2):
            highest = 8
        elif is_full_house(player2):
            highest = 7
        elif is_flush(player2):
            highest = 6
        elif is_straight(player2):
            highest = 5
        elif is_three_kind(player2):
            highest = 4
        elif is_two_pair(player2):
            highest = 3
        elif is_one_pair(player2):
            highest = 2

        print(player2, highest)

        if ph > highest:
            player1_victories += 1
        elif ph < highest:
            player2_victories += 1
        else:

            if ph == highest and ph > 0:
                if order.index(which_pair(player1)) > order.index(which_pair(player2)):
                    player1_victories += 1
                elif order.index(which_pair(player2)) > order.index(which_pair(player1)):
                    player2_victories += 1
                else:
                    print("Second highest... TODO")

            else:
                if high(player1) > high(player2):
                    player1_victories += 1
                elif high(player2) > high(player1):
                    print("player 2 wins")

    print("Player 1", player1_victories)
    print("Player 2", player2_victories)