#coding:utf-8
__author__ = 'jiliwei'
# 定义类的属性
# 1.直接在类里定义
# class Programer(object):
#     sex = "male"

# 2.在构造函数里定义
class Programer(object):
    # 构造函数
    def __init__(self,name,age,weight):
        self.name = name #可以公开访问
        self._age = age   #私有属性
        self.__weight = weight #部分私有属性

# 访问控制
# python其实没有访问控制
# 也没有提供私有属性的功能
# 全靠自觉。。。。。。。



