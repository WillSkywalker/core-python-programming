#!/usr/bin/env python
# Author: Will Skywalker

# Core Python Programming - Homework 8


import string


def ranran(start, end, increment=1):  # 8-1
    lst = []
    num = start
    while num < end:
        lst.append(num)
        num += increment
    return lst

def isprime(num):  # 8-4
    # for i in xrange(2, num/2):
    #     if num % i == 0:
    #         return False
    # return False
    return not any(num%i==0 for i in xrange(2,num/2+1))

def getfactors(num):  # 8-5
    return [f for f in xrange(1, num+1) if num%f==0]

def factorize(num):  # 8-6
    factors = reversed([f for f in getfactors(num) if isprime(f) and f!=1])
    answers = []
    for item in factors:
        while num % item == 0:
            num /= item
            answers.append(item)
    return answers

def isperfect(num):  # 8-7
    return num == sum(getfactors(num)[:-1])

def factorial(num):  # 8-8
    product = 1
    for i in xrange(1, num+1):
        product *= i
    return product

def fibonacci(index):  # 8-9
    a, b = 1, 1
    for i in xrange((index-1)/2):
        a += b
        b += a
    if index % 2 == 0:
        return b
    else:
        return a

def consonant_vowel(sentence):  # 8-10
    vovels = list('aeiouAEIOU')
    consonant = [s for s in list(string.letters) if s not in vovels]
    vovel_num, cons_num, word_num = 0, 0, 1
    for letter in str(sentence): 
        if letter in vovels:
            vovel_num += 1
        elif letter in consonant:
            cons_num += 1
        elif letter == ' ':
            word_num += 1
    return 'Vovels: %d, Consonants: %d, Words: %d' % (vovel_num, cons_num, word_num)

def name_process():  # 8-11
    number = int(raw_input('Enter total number of names: '))
    name_list = []
    mistake = 0
    for i in xrange(number):
        name = raw_input('Please enter name '+str(i+1)+': ')
        if not ',' in name:
            mistake += 1
            print '>> Wrong format... should be Last, First.'
            print '>> You have done this %d time(s) already. Fixing input...' % mistake
            name = name.split()
            name.reverse()
            name_list.append(', '.join(name))
        else:
            name_list.append(name)
    name_list.sort()#key=lambda x:x[x.index(',')+2]

    print 'The sorted list (by last name) is:'
    for name in name_list:
        print '    ' + name

def between_num(begin, end):
    decl, binl, octl, hexl, asciil = [], [], [], [], []
    ptab = False
    for num in xrange(begin, end+1):
        decl.append(num)
        binl.append(bin(num))
        octl.append(oct(num))
        hexl.append(hex(num))
        if chr(num) in string.printable:
            asciil.append(chr(num))
            ptab = True
        else:
            asciil.append('')

    if ptab:
        print '''
Decimal    Binary    Octal    Hexadecimal    ASCII
==================================================
'''
        for i in xrange(len(decl)):
            print '%5d     %8s     %5s  %8s    %5s' %(decl[i], binl[i], octl[i], hexl[i], asciil[i])
    else:
        print '''
Decimal    Binary    Octal    Hexadecimal
=========================================
'''
        for i in xrange(len(decl)):
            print '%5d     %8s     %5s  %8s' %(decl[i], binl[i], octl[i], hexl[i])









if __name__ == '__main__':
    # print consonant_vowel(raw_input('Sentence: '))
    # name_process()
    # print factorize(int(raw_input('Number: ')))
    between_num(int(raw_input('Begin: ')), int(raw_input('End: ')))

