#coding:utf-8

'''
from http://www.pythonchallenge.com/pc/def/equality.html
One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.
被三个大写守卫（字母）‘精确’地围绕的一个小写字母
'''
import urllib2
import re
SOURCE_TEXT = urllib2.urlopen('''http://www.pythonchallenge.com/pc/def/equality.html''')
rexp = r'(?<=[a-z][A-Z]{3})[a-z](?=[A-Z]{3}[a-z])'


def _find():
    source = re.findall(r'<!--.*?-->', (''.join(SOURCE_TEXT.readlines())).replace('\n', ''))[-1]
    txt = re.findall(rexp2, source)
    print ''.join(txt)          # linkedlist

if __name__ == '__main__':
    _find()
