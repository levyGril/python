#coding:utf-8
__author__ = 'jiliwei'

class Programer(object):
    hobby = "play Computer"

    def __init__(self,name,age,weight):
        self.name = name #可以公开访问
        self._age = age   #私有属性
        self.__weight = weight #部分私有属性
    def get_weight(self):
        return self.__weight

if __name__=="__main__":
    programer = Programer("Albert",25,80)
    print dir(programer)    #打印类的所有属性
    print programer.__dict__ #构造函数里面的所有属性
    print programer.get_weight()
    print programer._Programer__weight #

