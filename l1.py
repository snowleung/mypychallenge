# coding:utf-8

'''
from http://www.pythonchallenge.com/pc/def/map.html
'''


def solutions1():
    '''
    K -> M
    O -> Q
    E -> G
    '''
    text = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
    VAL = ord('M') - ord('K')
    output = ''.join([chr(ord(tt)+VAL) for tt in text])
    print output


def encrytpe():
    pass

if __name__ == '__main__':
    solutions1()
