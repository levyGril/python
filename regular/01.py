#coding:utf-8
__author__ = 'jiliwei'

import re
str1='imooc python'

# print str1.find('imooc')
pa = re.compile(r'imooc')
print type(pa) #<type '_sre.SRE_Pattern'>
ma = pa.match(str1)
print ma.group()
print ma.span()
print ma.string

print ma.re


