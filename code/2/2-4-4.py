print('''字典创建与操作''')
category = {'apple':'fruit','zootopia':'film','football':'sport'}
print(category['apple'])      # 查询键值对
# result: fruit
category['lemon'] = 'fruit'  # 插入新的键值对
print(category)
# result: {'zootopia': 'film', 'lemon': 'fruit', 'apple': 'fruit', 'football': 'sport'}
del category['lemon']       # 删除键值对
print(category)
# result: {'zootopia': 'film', 'apple': 'fruit', 'football': 'sport'}
print('-'*70)
items=[('height',1.80),('weight',124)]  # 也可以通过元组和dict()创建字典
D = dict(items)
print(D)
# result: {'weight': 124, 'height': 1.8}
print('-'*70)



print('''字典的遍历''')
keys = list(category.keys())
keys.sort()
print(keys)  #按照首字符的ASCII码排序
# result: ['zootopia', 'football', 'apple']
keys.sort(reverse=True)
print(keys)  #排序结果反转
# result: ['zootopia', 'football', 'apple']
# result:
def comp(str1,str2):   # 两个字符串的比较函数
    if str1[0] < str2[0]:  # 、如果str1的首字符比str2首字符的ASCII值小，那么str1排在str2前，否则排在后面
        return 1
    else:
        return -1

# keys.sort(comp)  # 自定义偏序关系，同样实现反向排序
print(keys)
# result: ['zootopia', 'football', 'apple']
for key in keys:    # 最后按照反向排序的顺序打印字典
    print((key,'=>',category[key]))
# result:
# ('zootopia', '=>', 'film')
# ('football', '=>', 'sport')
# ('apple', '=>', 'fruit')
