#!usr/bin/env python
# Author: Will Skyywalker

# Core Python Programming - Homework 11

import time

def my_max(*args):  # 11-3
    biggest = float('-inf')
    for istem in args:
        if item > biggest:
            biggest = item
    return biggest

def mult(x, y):  # 11-10
    return x * y

def factorial(x):
    if x == 1:
        return 1
    return x*factorial(x-1)


if __name__ == '__main__':
    t = time.time()
    print factorial(1000)
    print time.time() - t
    t = time.time()
    print reduce(lambda x, y: x*y, range(1,101))
    print time.time() - t
