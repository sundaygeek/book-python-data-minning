# -*- coding:utf-8 -*-
# 匿名函数
from math import log  #引入Python数学库的对数函数

# 此函数用于返回一个以base为底的匿名对数函数
def make_logarithmic_function(base):
    return lambda x:log(x,base)  

# 创建了一个以3为底的匿名对数函数，并赋值给了My_LF
My_LF = make_logarithmic_function(3)

# 使用My_LF调用匿名函数，参数只需要真数即可，底数已设置为3。而使用log()函数需要
# 同时指定真数和对数。如果我们每次都是求以3为底数的对数，使用My_LF更方便。
print My_LF(9)

# result: 2.0
