# coding:utf-8

'''
from http://www.pythonchallenge.com/pc/def/peak.html
'''

import urllib2
import pickle

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
SOURCE_TEXT = urllib2.urlopen(url)


def _serializaion():
    elms = pickle.load(SOURCE_TEXT)

    def print_it():
        for el in elms:
            print ''.join([e[0] * e[1] for e in el])
    print_it()

if __name__ == '__main__':
    _serializaion()
