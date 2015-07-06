# coding:utf-8

'''
from http://www.pythonchallenge.com/pc/def/map.html
'''

VAL = ord('M') - ord('K')
text = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''


def solutions2():
    '''
    twice
    '''
    output = ''.join(reduce(_select, list(text), []))  # tips, an trans table also.
    return output


def _select(l, char):
    if 'y' == char:
        l.append('a')  # { -> a
    elif 'z' == char:
        l.append('b')  # { -> b
    elif ord('a') <= ord(char) <= ord('z'):
        l.append(chr(ord(char) + VAL))
    else:
        l.append(char)
    return l


def trans_map(s='map'):
    import string
    tb = string.maketrans(text, solutions2())
    print string.translate('map', tb)  # map -> ocr


if __name__ == '__main__':
    trans_map()
