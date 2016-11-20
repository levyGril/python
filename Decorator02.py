#coding:utf-8
__author__ = 'jiliwei'

# 1.装饰器用来装饰函数
# 2. 返回一个函数对象
# 3. 被装饰函数标识符指向返回的函数对象
# 4. 语法糖 @deco
def deco(func):
    def in_deco(x,y):
        print("in deco")
        func(x,y)
    print ("call deco.........")
    return in_deco
@deco
def bar(x,y):
    print("in bar",x+y)
bar(1,2)

