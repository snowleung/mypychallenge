#coding:utf-8

'''
from http://www.pythonchallenge.com/pc/def/linkedlist.php
'''
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'
SOURCE_TEXT = urllib2.urlopen(url.format(12345))

def _try_nothing():
    '''
    12345 -> 44827 -> 45439 -> 94485
    '''
    for t in range(400):
        if t==0:
            content = urllib2.urlopen(url.format())

if __name__ == '__main__':
    _try_nothing()
