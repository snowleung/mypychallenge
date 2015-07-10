#!/usr/bin/env python
# coding:utf-8
'''
from http://www.pythonchallenge.com/pc/return/5808.html
'''
from PIL import Image
from itertools import product
from utils import cost_time
even = lambda num: num % 2 == 0
odd = lambda num: not even(num)
half = lambda x, y: (x / 2, y / 2) # too large
CAVE = Image.open('./cave.jpg')

@cost_time
def _even():
    '''
    even
    '''
    canve = Image.new(CAVE.mode, CAVE.size)
    pixel_matrix = product(range(CAVE.size[0]), range(CAVE.size[1]))
    for x,y in pixel_matrix:
        if even(x) and even(y):
            canve.putpixel(half(x, y), CAVE.getpixel((x, y)))
    canve.save('./evil_even.jpg')

@cost_time
def _odd():
    '''
    odd
    '''
    canve = Image.new(CAVE.mode, CAVE.size)
    pixel_matrix = product(range(CAVE.size[0]), range(CAVE.size[1]))
    for x,y in pixel_matrix:
        if odd(x) and odd(y):
            canve.putpixel(half(x, y), CAVE.getpixel((x, y)))
    canve.save('./evil_odd.jpg')


if __name__ == '__main__':
    _even()
    _odd()
