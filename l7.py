# coding:utf-8

'''
from http://www.pythonchallenge.com/pc/def/oxygen.html
'''
from PIL import Image
import urllib2
STEP = 7                        # why? becasue this is l7
grey = (0, 45)                  # grey start position:(x, y)


def download_file():
    try:
        open('./oxygen.png', 'r')  # file exists
    except IOError as ex:
        req = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png')
        with open('./oxygen.png', "wb") as local_file:
            local_file.write(req.read())


def gery_val(g):
    '''
    return grey RGB data
    '''
    img = Image.open('./oxygen.png')
    width = img.size[0]
    return [img.getpixel((i, g[1])) for i in range(0, width, STEP)]


def decode_RGB(rgb):
    return ''.join([chr(t[0]) for t in rgb])


def decode_list(s):
    import re
    return ''.join([chr(int(num)) for num in re.findall(r'\d+', s)])

if __name__ == '__main__':
    download_file()
    print decode_list(
        decode_RGB(
            gery_val(
                grey)))  # integrity
