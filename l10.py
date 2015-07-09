# coding:utf-8
'''
from http://www.pythonchallenge.com/pc/return/bull.html
tips: https://zh.wikipedia.org/wiki/%E5%A4%96%E8%A7%80%E6%95%B8%E5%88%97
'''


# [1,11,21,1121,111221]
# 1;      1
# 2;1&1 -> 11
# 3;2&1 -> 21
# 4;1&2,1&1 -> 1211
# 5;1&1,1&2,2&1 -> 111221
# 3&1,2&2,1&1 -> 312211
# 1&3,1&1,2&2,2&1 -> 13112221
# 1&1,1&3,2&1,3&2,1&1 -> 1113213211

'''
('str, shoot')
1
[('1', 1), ]                     # 11
[('1', 2), ]                     # 21
[('2', 1), ('1', 1)]             # 1211
[('1', 1), ('2', 1), ('1', 2)]   # 111221
'''

to_str = lambda s: (str(s[0]), str(s[1]))


def generate_desc(index, _init='1', res=None):
    if index == 0:
        return res
    res = []
    for s in _init:
        if res and ss[0] == s:
            ss = (s, ss[1] + 1)
            res[-1] = ss
        else:
            ss = (s, 1)
            res.append(ss)
    _init = _decode(map(to_str, res))
    return generate_desc(index - 1, _init=_init, res=res)


def _decode(cores):
    return reduce(lambda a, b: ''.join([a, ''.join([b[1], b[0]])]), cores, '')

if __name__ == '__main__':
    l = generate_desc(30)
    a30 = _decode(map(to_str, l))
    print len(a30)
