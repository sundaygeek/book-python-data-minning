# -*- coding:utf-8 -*-
import pandas as pd    # 为pandas取一个别名pd
data = {'id': ['Jack', 'Sarah', 'Mike'],
        'age': [18, 35, 20],
        'cash': [10.53, 500.7, 13.6]}
df = pd.DataFrame(data)    # 调用构造函数并将结果赋值给df
print(df)
# result:
#    age    cash     id
# 0   18   10.53   Jack
# 1   35  500.70  Sarah
# 2   20   13.60   Mike


df2 = pd.DataFrame(data, columns=['id', 'age', 'cash'],index=['one', 'two', 'three'])
print(df2)
# result:
#          id   age    cash
# one     Jack   18   10.53
# two    Sarah   35  500.70
# three   Mike   20   13.60


print(df2['id'])
# result:
# 0     Jack
# 1    Sarah
# 2     Mike
# Name: ID, dtype: object


s = pd.Series({'a': 4, 'b': 9, 'c': 16}, name='number')
print(s)
# result:
# a4
# b9
# c16
# Name: number, dtype: int64


print(s[0])
# result: 4
print(s[:3])
# result:
# a     4
# b     9
# c    16
# Name: number, dtype: int64


print(s['a'])
# result: 4
s['d'] = 25    # 如果系列中本身没有这个键值，则会新增一行
print(s)
# result:
# a     4
# b     9
# c    16
# d    25
# Name: number, dtype: int64


import numpy as np
print(np.sqrt(s))
# result:
# a    2.0
# b    3.0
# c    4.0
# d    5.0
# Name: number, dtype: float64
print(s*s)
# result:
# a     16
# b     81
# c    256
# d    625
# Name: number, dtype: int64


print(df['id'])    # 按列名访问(call-by-column)
# result:
# one       Jack
# two      Sarah
# three     Mike
# Name: ID, dtype: object

df['rich'] = df['cash'] > 200.0
print(df)
# result:
#    age    cash     id   rich
# 0   18   10.53   Jack  False
# 1   35  500.70  Sarah   True
# 2   20   13.60   Mike  False

del df['rich']
print(df)
# result:
#    age    cash     id
# 0   18   10.53   Jack
# 1   35  500.70  Sarah
# 2   20   13.60   Mike
