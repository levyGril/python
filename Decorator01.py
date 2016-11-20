#coding:utf-8
__author__ = 'jiliwei'

# 1.装饰器用来装饰函数
# 2. 返回一个函数对象
# 3. 被装饰函数标识符指向返回的函数对象
# 4. 语法糖 @deco

def dec(func):
    print ("call dec.......")
    def in_dec(*arg):
        print("in dec arg = ",arg)
        if(len(arg)==0):
            return 0
        for val in arg:
            if not isinstance(val,int):
                return 0
        return func(*arg)
    return in_dec

#执行顺序 dec->in_dec->my_sum
#@dec 等于 my_sum = dec(my_sum )
@dec
def my_sum(*arg):
    print("in my_sum,arg = ",arg)
    return sum(arg)
print(my_sum(1,2,3,4,5))


def my_average(*arg):
    return sum(arg)/len(arg)



