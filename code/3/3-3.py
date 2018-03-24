# -*- coding:utf-8 -*-
# 深复制与浅复制
import copy
list1 = [1,2,['a','b']]
list2 = list1
list3 = copy.copy(list1)
list4 = copy.deepcopy(list1)
list1.append(3)
list1[2].append('c')

print('list1 = ',list1)
print('list2 = ',list2)
print('list3 = ',list3)
print('list4 = ',list4)

# result: 
# list1 =  [1, 2, ['a', 'b', 'c'], 3]
# list2 =  [1, 2, ['a', 'b', 'c'], 3]
# list3 =  [1, 2, ['a', 'b', 'c']]
# list4 =  [1, 2, ['a', 'b']]
