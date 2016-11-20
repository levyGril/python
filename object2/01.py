#coding:utf-8
__author__ = 'jiliwei'

# magic method  带两个下划线
# 回收对象 __del__()

class Programer(object):
    # 创造对象
    def __new__(cls, *args, **kwargs):
        print 'call __new__ method'
        print args
        return super(Programer,cls).__new__(cls, *args, **kwargs)
    # 初始化对象
    def __init__(self,name,age):
        print 'call __init__ method'
        self.name = name
        self.age = age


# main函数
if __name__ =='__main__':
    programer = Programer('Albert',24)
    print programer.__dict__