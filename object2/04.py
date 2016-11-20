#coding:utf-8
__author__ = 'jiliwei'

# 类的访问属性

# 设置对象属性
# __setattr__(self,name,value)

# 方法一:错误
# def __setattr__(self,name,value):
#     setattr(self,name,value)
# 方法二：正确
# def __setattr__(self,name,value):
#     self.__dic__[name]==value

# 查询对象属性
# __getattr__(self,name)
# __getattribute__(self,name) 慎用

# 删除对象属性
#  __delattr__(self,name)

class Programer(object):
    # 构造函数
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __getattribute__(self, name):
        print 'call __getattribute__'
        return super(Programer,self).__getattribute__(name)

    def __setattr__(self, name, value):
         print 'call __setattr__'
         self.__dict__[name]=value


if __name__ == '__main__':
    p = Programer('Albert',23)
    print p.name



