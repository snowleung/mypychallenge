# coding:utf-8
'''
from http://www.pythonchallenge.com/pc/def/channel.html
'''
import re
import zipfile

pattern = r'\d+'
zdata = zipfile.ZipFile('/Users/samleung/Desktop/channel.zip')
zip_dir = dict.fromkeys(zdata.namelist())
START = None                 # at README.txt


def find_start():
    start_next = re.findall(pattern, zdata.read('readme.txt'))  # at README.txt
    global START
    START = start_next[1]
    print START


def using_zip():
    '''
    use zipfile module
    '''
    namelist = []
    find_start()
    name = '{}.txt'.format(START)
    while 1:
        content = zdata.read(name)
        try:
            name = re.findall(pattern, content)[0]  # know need to collect the comments
            name = '{}.txt'.format(name)
        except IndexError as e:
            print content
            return namelist
        namelist.append(name)
        print content, name


def collect_comments(namelist):
    cc = []
    for n in namelist:
        cc.append(zdata.NameToInfo[n].comment)
    return cc

if __name__ == '__main__':
    print ''.join(collect_comments(using_zip()))  # got hockey, but build by oxygen
