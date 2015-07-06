#coding:utf-8

'''
from http://www.pythonchallenge.com/pc/def/ocr.html
'''
import urllib2
import re
SOURCE_TEXT = urllib2.urlopen('''http://www.pythonchallenge.com/pc/def/ocr.html''')


def find_content():
    source = re.findall(r'<!--.*?-->', (''.join(SOURCE_TEXT.readlines())).replace('\n', ''))[1]
    txt = re.findall(r'[a-zA-Z]', source)
    print ''.join(txt)          # equality

if __name__ == '__main__':
    find_content()
