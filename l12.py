# coding:utf-8
'''
from http://www.pythonchallenge.com/pc/return/evil.html
'''
gfx = open('./evil2.gfx', 'rb')


def _gfx(gfx):
    data = gfx.read()
    for i in range(5):
        with open('evil_{}.jpg'.format(i), 'wb') as ff:
            ff.write(data[i::5])

if __name__ == '__main__':
    _gfx(gfx)                   # disproportional
