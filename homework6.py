#!/usr/bin/env python
# Author: Will Skywalker

# Core Python Programming - Homework 6

import string, keyword


def idcheck():  # 6-2
    alphas = string.letters + '_'
    nums = string.digits

    print 'Welcome to the Identifier Checker v0.1'
    print 'Testees must be at least 2 chars long.'
    myInput = raw_input('Identifier to test? ')

    if len(myInput) > 1:
        if myInput in keyword.kwlist:
            print 'invalid: identifier can\'t be a keyword'
            return False
        elif myInput[0] not in alphas:
            print 'invalid: first symbol must be alphabetic'
            return False
        else:
            for otherChar in myInput[1:]:
                if otherChar not in alphas + nums:
                    print 'invalid: remaining symbols must be alphabetic'
                    return False
            else:
                print 'okay as an identifier'
                return True

    elif len(myInput) == 1:
        if myInput not in alphas:
            print 'invalid: first symbol must be alphabetic'
            return False
        else:
            print 'okay as an identifier'
            return True


def str_strip(target):  # 6-6
    tal = list(target)
    nlw = []
    for i in xrange(len(tal)):
        if tal[i] != ' ':
            nlw.append(tal[i])
    return ''.join(nlw)


def buggy():  # 6-7
    
    num_str = raw_input('Enter a number: ')
    num_num = int(num_str)

    fac_list = range(1, num_num+1)
    print 'BEFORE:', str(fac_list)

    # i = 0

    # while i < len(fac_list):
    #     if num_num % fac_list[i] == 0:
    #         del fac_list[i]

    #     i = i + 1
    end_list = []
    for i in fac_list:
        if num_num % i != 0:
            end_list.append(i)


    print 'AFTER:', str(end_list)


def num_to_words(num):  # 6-8
    convert_dict = {1: 'one',
                    2: 'two',
                    3: 'three',
                    4: 'four',
                    5: 'five',
                    6: 'six',
                    7: 'seven',
                    8: 'eight',
                    9: 'nine',
                    0: 'zero'}
    result = []
    for n in list(str(num)):
        result.append(convert_dict[int(n)])
    return '-'.join(result)


def min_to_hrs(minute):  # 6-9
    hour, minute = divmod(float(minute), 60)
    return hour, minute


def ip_convert(ip):  # 6-11
    if '.' in ip:
        new_ip = ip.split('.')
        tar = []
        for s in new_ip:
            tar.append(s.zfill(3))
        return ''.join(tar)
    elif len(ip) == 12:
        new_ip = list(ip)
        for i in range(3, 15, 4):
            new_ip.insert(i, '.')
        return ''.join(new_ip)


def findchr(string, char):  # 6-12 (a)
    for i in xrange(len(string)):
        if string[i] == char:
            return i
    return -1


def rfindchr(string, char):  # 6-12 (b)
    for i in xrange(len(string)-1, -1, -1):
        if string[i] == char:
            return i
    return -1


def subchr(string, origchar, newchar):  # 6-12 (c)
    for i in xrange(len(string)):
        if string[i] == origchar:
            string[i] = newchar


def myPop(target_list):  # 6-17
    poped = target_list[-1]
    del target_list[-1]
    return poped


def multiColumn(data, column):  # 6-19
    output = [list() for i in xrange(column)]
    data_index = 0
    rows = len(data)//column
    for i in xrange(column):
        for ldx in xrange(rows):
            output[i].append(data[data_index])
            data_index += 1
    if data_index < len(data):
        output.append([])
        for i in xrange(data_index, len(data)):
            output[-1].append(data[i])

    for outer_idx in xrange(rows):
        output_str = ''
        for inter_idx in xrange(column):
            output_str += str(output[inter_idx][outer_idx])
            output_str += '    '
        print output_str
    if data_index < len(data):
        output_str = ''
        for item in output[-1]:
            output_str += str(item)
            output_str += '    '
        print output_str

    # return output



if __name__ == '__main__':
    multiColumn(eval(raw_input()), 3)
