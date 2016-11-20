#coding:utf-8
__author__ = 'jiliwei'

#python 常见错误
#1. nameError
#2 if true:语法错误syntax
#3. f=open("test.txt") io error 文件不存在
#4 10/0 : zerpDivisionError
#5 a = int("dd") : vauleError

#python Exception
# try-except

#case1
# try:
#     undef
# except:  #不加参数，捕获所有异常
#     print("catch an exception1")

#case2
# try:
#     if undef
# except:  #不加参数，捕获所有异常
#     print("catch an exception2")

#case3
# try:
#     undef
# except NameError ,e:  #不加参数，捕获所有异常
#     print"catch an exception1",e

#case4
try:
    undef
except IOError,e:  #不加参数，捕获所有异常
    print"catch an exception1",e


# try-except-else-finally使用
# try:
#     try_suite
# except:
#     do_except
# else:
#     do_else
# finally:
#     do_finally
#
# 1. 若try语句没有捕获异常，执行完try代码段后，执行else代码段，最后执行 finally
# 2. 若try语句捕获到异常，首先执行except处理错误，然后执行finally



