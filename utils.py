#coding:utf-8

from datetime import datetime

def cost_time(func):
    def _cost_time(*args, **kwargs):
        print '='*10,
        print 'start:func: {}'.format(func.__name__), 
        print '='*10
        n = datetime.now()
        r = func(*args, **kwargs)
        print 'cost :{}'.format(datetime.now()-n)
        print '='*10,
        print 'end:func: {}'.format(func.__name__), 
        print '='*10
        return r
    return _cost_time
