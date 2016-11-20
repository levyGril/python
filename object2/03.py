#coding:utf-8
__author__ = 'jiliwei'

# 类的展现

# 转换为字符串
# __str__
# __repr__
# __unicode__

# 展现对象的属性
# __dir__


class Programer(object):
    def __init__(self,name,age):
        self.name = name
        if isinstance(age,int):
            self.age = age
        else:
            raise Exception('age must be int')
    def __str__(self):
        return '%s is %s years old'%(self.name,self.age)
    def __dir__(self):
        return self.__dict__.keys()

if __name__=='__main__':
    programer1 = Programer('Alert',25)
    print programer1
    print dir(programer1)
