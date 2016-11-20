#coding:utf-8
__author__ = 'jiliwei'
import math
def my_sum(*arg):
    print("in my_sum,arg = ",arg)
    return sum(arg)
def my_average(*arg):
    return sum(arg)/len(arg)

# 闭包
def dec(func):
    def in_dec(*arg):
        print("in dec arg = ",arg)
        if(len(arg)==0):
            return 0
        for val in arg:
            if not isinstance(val,int):
                return 0
        return func(*arg)
    return in_dec

my_sum = dec(my_sum) #my_sum = in_dec(*arg)
print (my_sum(1,2,3,4,5))

my_average = dec(my_average)
print (my_average(1,2,3,4,5))
# print (my_average())

