#!usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Will Skyywalker

# Core Python Programming - Homework 18

import re
import urllib2
import threading
import webbrowser
import codecs
import Queue



# class ThreadFund(threading.Thread):
#     """docstring for ThreadFund"""
#     def __init__(self, arg):
#         super(ThreadFund, self).__init__()
#         self.arg = arg
def find_song(hand):
    sub = []
    for line in hand:
        t = re.search(r'<a title=".+" href="http://www\.xiami\.com/song/[0-9]+', line)
        if t:
            # print codecs.encode(line, 'utf-8')
            st = t.group()
            # print codecs.encode(re.search(r'".+?"', st).group()[1:-1], 'utf-8')
            sub.append((re.search(r'".+?"', st).group()[1:-1], re.search(r'href=".+', st).group()[6:]))
    return sub


class SongThread(threading.Thread):
    def __init__(self, func):
        super(SongThread, self).__init__()
        self.arg = arg
        



if __name__ == '__main__':
    # fhand = urllib2.urlopen('http://www.xiami.com/space/lib-song')
    fhand = codecs.open('songs.html', encoding='utf-8')
    print find_song(fhand)

