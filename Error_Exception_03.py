#coding:utf-8
__author__ = 'jiliwei'

# with-as 语句
# 格式
# with context[as var]:
#     with_suite

# 1. with语句用来代替try-except-finally语句，使代码更加简洁
# 2.context表达式是一个对象
# 3.var用来保存context返回对象，单个返回值或者元祖
# 4.with_suite使用var变量来对context返回的对象进行操作呢

#case1
with open("1.txt") as f:
    for line in f.readlines():
        print line