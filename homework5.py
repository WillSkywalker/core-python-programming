#!/usr/bin/env python
# Author: Will Skywalker

# Core Python Programming - Homework 5

import random

def timing(a, b):
    return a * b


def ifLongYear(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else:
        return False


def mostCoin(dollar):
    cent = float(dollar) * 100
    (num_25, cent) =  divmod(cent, 25)
    (num_10, cent) = divmod(cent, 10)
    (num_5, cent) = divmod(cent, 5)
    (num_1, cent) = divmod(cent, 1)
    return sum((num_25, num_10, num_5, num_1))


def crazyRandom():
    randList = []
    usingList = []
    for i in xrange(random.randrange(2, 101)):
        randList.append(random.randrange(0, 2**31))
    for i in xrange(random.randrange(1, 101)):
        usingList.append(randList[random.randrange(len(randList))])
    return sorted(usingList)


print crazyRandom()
print mostCoin(raw_input())
