#!usr/bin/env python
# Author: Will Skyywalker

# Core Python Programming - Homework 13

from math import sqrt, atan, pi
from time import ctime

class MoneyFmt(float):  # 13-3, 13-17

    def __init__(self, amount, bracket=False):
        super(MoneyFmt, self).__init__()
        self._amount = amount
        self._bracket = bracket

    def __str__(self):
        if self._bracket and repr(self._amount)[0] == '-':
            string = '<'+str(round(self._amount, 2))[1:]+'>'
        else:
            string = str(round(self._amount, 2))
        formed = list(string.split('.')[0])
        for i in xrange(len(formed)-3, 0, -3):
            formed.insert(i, ',')
        return '$'+''.join(formed)+'.'+string.split('.')[1]

    def __repr__(self):
        return str(round(self._amount, 2))

    def __add__(self, another):
        return MoneyFmt(self._amount + another)

    def __sub__(self, another):
        return MoneyFmt(self._amount - another)

    def __abs__(self):
        return MoneyFmt(abs(self._amount))

    def __mul__(self, another):
        return MoneyFmt(self._amount * another)

    def __div__(self, another):
        return MoneyFmt(self._amount / another)

    def __pow__(self, another):
        return MoneyFmt(self._amount ** another)

    def __nonzero__(self):
        return True if self._amount != 0 else False

    def update(self, new):
        self._amount = new


class Point(object):   # 13-5
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, another):
        return self.__class__(self.x+another.x, 
                              self.y+another.y)

    def __sub__(self, another):
        return self.__class__(self.x-another.x, 
                              self.y-another.y)

    def __abs__(self):
        if self.x >= 0 and self.y >= 0:
            return self
        return self.__class__(abs(self.x), abs(self.y))

    def __pow__(self, another):
        return sqrt((self-another).x**2 + \
                    (self-another).y**2)

    def __str__(self):
        return str((self.x, self.y))
    __repr__ = __str__



class StraightLine(object):   # 13-6
    def __init__(self, point_1, point_2):
        self._point_1 = point_1
        self._point_2 = point_2

    def __str__(self):
        return str(((self._point_1), (self._point_2)))

    def length(self):
        return self._point_1 ** self._point_2

    def slope(self):
        return atan(abs(self._point_1-self._point_2).x/\
               abs(self._point_1-self._point_2).y)/pi*180


class Date(object):   # 13-7
    def __init__(self, now=ctime()):
        self._now = now
    
    def update(self, now=ctime()):
        self._now = now

    def display(self, mode='MDY'):
        times = self._now.split()
        # print times
        for c in mode:
            if c == 'M':
                print times[1],
            elif c == 'D':
                print times[2],
            elif c == 'Y':
                print times[4],
            elif c == 'O':
                print times[0],


class PanStack(list):   # 13-10
    """docstring for Stack"""
    def __init__(self, arg):
        super(PanStack, self).__init__(arg)
        # self.arg = arg

    def pop(self):
        return super(PanStack, self).pop(-1)

    def push(self, value):
        super(PanStack, self).append(value)

    def shift(self):
        return super(PanStack, self).pop(0)

    def unshift(self, value):
        super(PanStack, self).insert(0, value)
    
    def peek(self):
        return self[0]

    def isempty(self):
        return bool(self)


class CapOpen(object):   # 13-16
    def __init__(self, fn, mode='r', buf=-1):
        self.file = open(fn, mode, buf)

    def __str__(self):
        return str(self.file)

    def __repr__(self):
        return repr(self)

    def write(self, line):
        self.file.write(line.upper())

    def writelines(self, sequence, sep=''):
        for line in sequence:
            self.file.write(line.upper()+sep)

    def __getattr__(self, attr):
        return getattr(self.file, attr)


class SimDict(dict):   # 13-19
    def __init__(self, arg):
        super(SimDict, self).__init__(arg)

    def keys(self):
        return sorted(super(SimDict, self).keys())    



class Time60(object):
    def __init__(self, *args, **kwargs):
        self.hr = 0
        self.mint = 0
        if kwargs:
            self.hr = kwargs['hr']
            self.mint = kwargs['min']
        if len(args) == 1:
            if isinstance(args[0],str):
                temp_list = args[0].split(':')
                self.hr = int(temp_list[0])
                self.mint = int(temp_list[1])
            else:
                self.hr = args[0][0]
                self.mint = args[0][1]
        elif len(args) >= 2:
            self.hr = args[0]
            self.mint = args[1]

    def __str__(self):
        return '%02d:%02d' % (self.hr, self.mint)

    def __repr__():
        return str([self.hr, self.mint])

    def __add__(self, other):
        output = divmod(self.mint+other.mint, 60)
        return self.__class__(self.hr + other.hr + output[0],
                              output[1])

    def __iadd__(self, other):
        output = divmod(self.mint+other.mint, 60)
        self.hr += other.hr + output[0]
        self.mint = output[1]
        return self
                




if __name__ == '__main__':
    a = Time60('17:55')
    b = Time60('5:37')
    # a.writelines('euidwh ufyo you fucking sob', '\n')
    # print a * 3
    print a + b

