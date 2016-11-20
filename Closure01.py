#coding:utf-8
__author__ = 'jiliwei'
# 函数的实质与属性
# 1. 函数是一个对象
# 2. 函数执行完成后内部变量回收
# 3. 函数属性
# 4. 函数返回值

# 闭包的作用
# 1. 封装
# 2. 代码复用
def set_passline(passline):
    def cmp(val):
        if(val>=passline):
            print("%d pass"%val)
        else:
            print("%d fail"%val)
    return cmp
func_100 = set_passline(60)
func_150 = set_passline(90)
func_100(89)
func_150(89)


