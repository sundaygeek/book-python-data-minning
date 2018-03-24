# -*- coding:utf-8 -*-
from scipy import poly1d
p = poly1d([3, 4, 5])
print(p)
# result:
#    2
# 3 x + 4 x + 5

print(p*p)
# result:
#   4      3      2
# 9 x + 24 x + 46 x + 40 x + 25

print(p.integ(k=6))    # 求p(x)的不定积分，指定常数项为6
# result:
#   3   2
# 1 x + 2 x + 5 x + 6
print(p.deriv())    # 求p(x)的一阶导数
# result:
# 6 x + 4

p([4, 5])    # 计算每个值代入p(x)的结果
# result:
# array([ 69, 100])



# -*- coding:utf-8 -*-
import numpy as np

def addsubtract(a, b):    # 按照原始定义，仅接受可比较的数字作为参数
    if a > b:
        return a - b
    else:
        return a + b

vec_addsubtract = np.vectorize(addsubtract)
print(vec_addsubtract([0, 3, 6, 9], [1, 3, 5, 7]))
# result:
# [1 6 1 2]
