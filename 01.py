#coding:utf-8
__author__ = 'jiliwei'
passline = 60
def func(val):
    print ('%x'%(val))
    print("%x"%(val))
    if(val>=passline):
        print ("pass")
    else:
        print("fail")
    def in_func():
        print (val)
    in_func()
    return in_func
f = func(89)
f()
print (f.__closure__)
