#coding:utf-8
__author__ = 'jiliwei'

# 类与运算符
# 用magic method 实现的好处
# 1. 优雅
# 2. 被python的标准语法支持

# s = "test"
# print s==s
# print dir(s)

# __cmp__(self,other) 比较所有的比较情况
# __eq__(self,other) 相等
# __lt__(self,other) 小于
# __gt__(self.other) 大于
# 算术运算
# __add__(self,other) +
# __sub__(self,other) -
# __mul__(self,other) *
# __div__(self,other) /

# 逻辑运算
# __or__(self,other)  逻辑或
# __and__(self,other) 逻辑与

#case
class Programer(object):
    def __init__(self,name,age):
        self.name = name
        if isinstance(age,int):
            self.age = age
        else:
            raise Exception('age must be int')

    def __eq__(self, other):
        if isinstance(other,Programer):
            if self.age == other.age:
                return True
            else:
                return False
        else:
            raise Exception('The Type of object must be Programer')

    def __add__(self, other):
        if isinstance(other,Programer):
            return self.age+other.age
        else:
            raise Exception('The Type of object must be Programer')

if __name__=='__main__':
    programer1 = Programer('Alert',25)
    programer2 = Programer('Bill',30)
    print programer1 ==programer2
    print programer1+programer2



