# coding:utf-8
'''
from http://www.pythonchallenge.com/pc/def/channel.html
'''
import re
import urllib2
import zipfile

pattern = r'\d+'
zdata = None
zip_dir = None
START = None

def init():
    # download_file
    req = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/channel.zip')
    with open('./channel.zip', "wb") as local_file:
        local_file.write(req.read())
    global zdata
    global zip_dir
    zdata = zipfile.ZipFile('./channel.zip')
    dict.fromkeys(zdata.namelist())

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
    init()
    print ''.join(collect_comments(using_zip()))  # got hockey, but build by oxygen
