#!/usr/bin/env python
# Author: Will Skywalker

# Core Python Programming - Homework 7


def key_value(raw):  # 7-7
    output = {}
    for key in raw.keys():
        output[raw[key]] = key
    return output


def huRs():  # 7-8
    db = {}
    while True:
        print 'Input "q" to quit'
        name = raw_input('Enter the name:')
        num = raw_input('Enter the number: ')
        if name.lower()[0] == 'q' or num.lower()[0] == 'q':
            break
        db[name] = int(num)

    print '''
    Choose output method
    a) sort by names
    b) sort by numbers
'''
    choose = raw_input('Your method: ')
    if choose == 'b':
        db = key_value(db)
    for k in sorted(db):
        print k, db[k]


def tr(srcstr, dststr, string, cap=True):  # 7-9
    dlength = len(srcstr)
    charset = {}
    for i in xrange(dlength):
        try:
            charset[srcstr[i]] = dststr[i]
        except IndexError:
            charset[srcstr[i]] = ''
    if cap:
        cap = {}
        for k in charset:
            cap[k.upper()] = charset[k].upper()
        charset.update(cap)
    new_strlist = []
    for c in string:
        if c in charset:
            new_strlist.append(charset[c])
        else:
            new_strlist.append(c)
    return ''.join(new_strlist)


def rot13(raw):  # 7-10 
    from string import letters
    small = letters[:26]
    capital = letters[26:]
    charset = {}

    for idx in xrange(26):
        rot = idx + 13
        if rot >= 26:
            rot -= 26
        charset[small[idx]] = small[rot]
        charset[capital[idx]] = capital[rot]

    new_strlist = []
    for c in raw:
        if c in charset:
            new_strlist.append(charset[c])
        else:
            new_strlist.append(c)
    return ''.join(new_strlist)


def calculator(string):  # 7-15
    pass




if __name__ == '__main__':
    print rot13(raw_input('Input the string: '))
    # print tr('atlgpeiou',
    #          'uzrdf', 
    #          raw_input('Sentences: '))



