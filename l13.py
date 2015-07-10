#coding:utf-8
'''
from http://www.pythonchallenge.com/pc/return/disproportional.html
'''

import xmlrpclib
link = '''http://www.pythonchallenge.com/pc/phonebook.php'''
def conn():
    return xmlrpclib.Server(link)
if __name__ == '__main__':
    s = conn()
    print s.phone('Bert')       # from evil4.jpg, answer 555-ITALY
