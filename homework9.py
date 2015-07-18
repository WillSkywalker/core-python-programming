#!/usr/bin/env python
# Author: Will Skywalker

# Core Python Pogramming - Homework 9

import os, imp
import string, random


def file_fliter(name):  # 9-1
    fhand = open(name)
    for line in fhand:
        if line[0] != '#':
            print line,
    fhand.close()


def read_file():  # 9-2
    fhand = open(raw_input('File name: '))
    number = int(raw_input('Line number: '))
    i = 0
    for line in fhand:
        if i < number:
            print line,
            i += 1
    fhand.close()


def line_number(fhand=None):  # 9-4
    if not fhand:
        fhand = open(raw_input('File name: '))
    idx = 0
    for line in fhand:
        print line,
        if idx >= 24:
            ans = raw_input('Do you want to continue? (y/n) ')
            if ans[0] == 'y':
                idx = 0
            else:
                break
        else:
            idx += 1
    fhand.close()


def compare_files():  # 9-6
    file_1 = [line.rstrip() for line in open(raw_input('First file: '))]
    file_2 = [line.rstrip() for line in open(raw_input('Second file: '))]
    file_1.close()
    file_2.close()
    idx = 0
    for i in xrange(max(len(file_1), len(file_2))):
        if file_1[i] != file_2[i]:
            break
    else:
        print "Two files are same."
        return None

    print i+1

   
def services_comp():  # 9-7
    ports = set([])
    fhand_s = open('/etc/services')
    exp = file('Port_Numbers.txt', 'w')
    for line in fhand_s:
        if line[0] not in string.letters:
            continue
        fragments = line.split()
        exp.write(fragments[1][:-4]+' '+fragments[0]+'\n')
    fhand_s.close()
    exp.close()


def module_doc():  # 9-9
    output = open('Docstring_of_Standard_Library.txt', 'w')
    os.chdir('/usr/lib/python2.7')
    for filename in os.listdir('/usr/lib/python2.7'):
        if filename[-3:] == '.py':
            fhand = open(filename)
            docs = ''
            is_doc = False
            for line in fhand:
                if "'''" in line[:4] or '"""' in line[:4]:
                    if line[-4:-1] == "'''" or line[-4:-1] == '"""' and len(line)>4:
                        docs += line[:-4] + '\n'
                        break
                    if is_doc:
                        break
                    is_doc = True
                elif line[-4:-1] == "'''" or line[-4:-1] == '"""':
                    docs += line
                    break
                if is_doc:
                    docs += line
            fhand.close()
            if docs:
                output.write(filename[:-3]+
                '\n=====================================================================\n'
                +docs.lstrip('r\'"')+'\n\n\n\n\n')
            else:
                output.write(filename[:-3]+
                '\n=====================================================================\n'
                +'No docstring. \n'+'\n\n\n\n\n')


def bookmark_manage():  # 9-11
    '''
    !!! This program needs to be TOTALLY REWRITTEN !!!
    '''
    print '''
Bookmark Manager
=========================================
'''
    main_menu = '''
(L)ook
(A)dd
(E)dit
(S)earch
(Q)uit

'''
    while True:
        choice = raw_input(main_menu).lower()
        if choice[0] == 'l':
            try:
                fhand = open('bookmarks.txt', 'r')
            except IOError:
                new = open('bookmarks.txt', 'w')
                new.close()
                fhand = open('bookmarks.txt', 'r')
            print
            for item in fhand:
                print item.rstrip()
            fhand.close()
        elif choice[0] == 'a':
            try:
                fhand = open('bookmarks.txt', 'a')
            except IOError:
                new = open('bookmarks.txt', 'w')
                new.close()
                fhand = open('bookmarks.txt', 'a')
            new_item = (raw_input('Name: '), raw_input('Address: '))
            fhand.write(new_item[0]+': '+new_item[1]+'\n')
            print 'New bookmark added! \n'
        elif choice[0] == 'e':
            try:
                fhand = open('bookmarks.txt', 'r+')
            except IOError:
                print 'No bookmark yet!\n'
                continue
            for item in fhand:
                print item
            name = raw_input('Input name to change: ')
            for idx, item in enumerate(fhand):
                if item.split(': ')[0] == name:
                    fhand.seek(idx)
                    new_add = raw_input('New address: ')
                    fhand.write(item.split(': ')[0]+': '+new_add+'\n')
            fhand.close()
        else:
            print 'Quitted!'
            break
            

def list_argv():  # 9-13
    from sys import argv
    for a in argv:
        print a

def copy_files():  # 9-15
    while True:
        try:
            file_1 = open(raw_input('Input file: '))
            break
        except IOError:
            print 'File doesn\'t exist!'
    file_2 = open(raw_input('Copy to: '), 'w')
    for line in file_1:
        file_2.write(line)
    file_1.close()
    file_2.close()


def text_editor():  # 9-17
    main_menu = '''
===========================================================
(C)reate new file
(S)how a file
(E)dit a file
(Q)uit
===========================================================
'''
    while True:
        mode = raw_input(main_menu)[0].lower()
        if mode == 'q':
            break
        filename = raw_input('File name: ')
        if mode == 'c':
            if not os.path.isfile(filename):
                fhand = open(filename, 'w')
                print 'Input\nPrint \':q!\' to exit\n'
                line = ''
                while line != ':q!':
                    fhand.write(line)
                    line = raw_input()+'\n'
                fhand.close()
                continue
            print 'File name exists!'
        elif mode == 's':
            if os.path.isfile(filename):
                fhand = open(filename)
                for line in fhand:
                    print line,
                print
                fhand.close()
            else:
                print 'File doesn\'t exist!'
        elif mode == 'e':
            if os.path.isfile(filename):
                fhand = open(filename, 'r+')
                for idx, line in enumerate(fhand, start=1):
                    print '%4d   '%idx, line,
                fhand.seek(0, 0)
                lines = fhand.readlines()
                fhand.close()
                while raw_input('Edit a line? (y/n) ')[0].lower() == 'y':
                    line_num = int(raw_input('Choose the line number to change: '))
                    print lines[line_num-1],
                    lines[line_num-1] = raw_input('Input\n') + '\n'
                fhand = open(filename, 'w')
                fhand.writelines(lines)
                fhand.close()


def search_file():  # 9-18
    count = 0
    target = chr(int(raw_input('Chosen ASCII Code (0-255): ')))
    for line in open(raw_input('File Name: ')):
        for c in line:
            if c == target:
                count += 1
    print 'Number: %d' %count


def create_file():  # 9-19
    test = ''
    used_num = [-1]
    field = range(255)
    target = int(raw_input('Chosen ASCII Code (0-255): '))
    field.remove(target)
    times = int(raw_input('Times of appearance: '))
    length = int(raw_input('Length:'))
    for i in xrange(length):
        test += chr(random.choice(field))
    for i in xrange(times):
        temp = list(test)
        p = -1
        while p in used_num:
            p = random.randrange(length)
        temp[p] = chr(target)
        test = ''.join(temp)
    print test



if __name__ == '__main__':
    # file_fliter(raw_input('File name: '))
    text_editor()
