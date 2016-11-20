#coding:utf-8
__author__ = 'jiliwei'

# 定义类的方法

# class Example(object):
#     def add(self): #公有
#         pass
#     def _minus(self):  #私有
#         pass
#     def __multiply(self):
#         pass
# 类的装饰器 ，调用的时候用类名，而不是某个对象
# @classmethod
# @property 像访问属性一样调用方法


# case1
class Programer(object):
    hobby = "play Computer"

    def __init__(self,name,age,weight):
        self.name = name #可以公开访问
        self._age = age   #私有属性
        self.__weight = weight #部分私有属性

    @classmethod
    def get_hobby(cls):
        return cls.hobby

    @property
    def get_weight(self):
        return self.__weight

    def self_introduction(self):
        print 'My Name is %s\nI am %s years old\n'%(self.name,self._age)

if __name__=="__main__":
    programer = Programer("Albert",25,80)
    print dir(programer)    #打印类的所有属性
    print programer.get_weight
    print Programer.get_hobby()
    programer.self_introduction()

