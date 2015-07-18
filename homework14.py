#!usr/bin/env python
# Author: Will Skyywalker

# Core Python Programming - Homework 13

import os, sys
import subprocess


def tesexi():
    print '''
Ob-La-Di, Ob-La-Da, 
Life goes on bro!'''
    sys.exit()
sys.exitfunc = tesexi


f = subprocess.Popen((raw_input()), 
                     stdout=subprocess.PIPE).stdout
for i in f:
    print i,
