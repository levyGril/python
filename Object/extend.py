#coding:utf-8
__author__ = 'jiliwei'

# 子类的类型判断
# isinstance
# issubclass

# python可以多继承

# case
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

class BackendProgramer(Programer):
    # 构造函数
    def __init__(self,name,age,weight,language):
        super(BackendProgramer,self).__init__(name,age,weight)
        self.language = language

if __name__=="__main__":
    programer = BackendProgramer("Albert",25,80,'Python')
    print dir(programer)    #打印类的所有属性
    print programer.__dict__
    print type(programer)
    print isinstance(programer, Programer)