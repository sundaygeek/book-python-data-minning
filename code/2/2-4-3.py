print('''元组''')
tuple1 = ('A','我')
print(len(tuple1))
# result: 2
tuple2 = tuple1+(6,6,'的')
print(tuple2)
# 注意我的机子系统的中文默认编码是cp936，可以使用'中文'.decode('cp936')转车unicode编码
# result:('A', '\xce\xd2', 6, 6, '\xb5\xc4')
tuple1 = ('A','我'.encode('utf8'))
print(tuple1)
# result： ('A', u'\u6211')
tuple3 =(1,)   # 创建仅有一个数据的元组
print(tuple3)
# result:(1,)
tuple4 = 3*(1+5,) # 一个逗号完全改不了表达式的值
print(tuple4)
# result: (6, 6, 6)
print(tuple(list(tuple4)))  # tuple函数可以将其他序列类型转变为元组
# result: (6, 6, 6)
print(tuple4[0])   # 同样可以使用索引
# tuple4[0] = 7 错误，不能改变元组的数据
print(tuple4.count(6))   # 同样有count()函数
# result: 3 
