#!/usr/bin/env python
# Author: Will Skywalker

# Core Python Pogramming - Homework 10

import math

def refined_open(filename, mode='r'):
    try:
        fhand = open(filename, mode)
    except (ValueError, TypeError), e:
        fhand = None
    return fhand

def safe_input():
    try:
        output = raw_input()
    except (EOFError, KeyboardInterrupt), e:
        output = None
    return output

def safe_sqrt(num):
    try:
        output = math.sqrt(num)
    except ValueError, e:
        output = complex(imag=math.sqrt(abs(num)))
    return output


if __name__ == '__main__':
    print safe_sqrt(int(raw_input('Number: ')))