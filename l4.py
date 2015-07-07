# coding:utf-8

'''
from http://www.pythonchallenge.com/pc/def/linkedlist.php
'''

import re
import urllib2

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'
SOURCE_TEXT = urllib2.urlopen(url.format(12345))

def _try_nothing(_next=12345):
    while 1:
        req = urllib2.urlopen(url.format(_next))
        content = ''.join(req.readlines())
        print content           # next=66831, peak.html
        _next = re.findall(r'\d+', content)[0]

if __name__ == '__main__':
    _try_nothing()
