# -*- coding:utf-8 -*-
import numpy as np   # 导入模块

print('''创建数组''')
arr1 = np.array([2,3,4])    # 通过列表创建数组
arr2 = np.array([(1.3,9,2.0),(7,6,1)])    # 通过元组创建数组
arr3 = np.zeros((2,3))    # 通过元组(2, 3)生成全零矩阵
arr4 = np.identity(3)    # 生成3维的单位矩阵
arr5 = np.random.random(size = (2,3)) # 生成每个元素都在[0,1]之间的随机矩阵
arr6 = np.arange(5,20,3)  # 生成等距序列,参数为起点,终点,步长值.含起点值，不含终点值
arr7 = np.linspace(0,2,9)  # 生成等距序列,参数为起点,终点,步长值.含起点值和终点值
print(arr1)
# result:
# [2 3 4]
print(arr2)
# result:
# [[ 1.3  9.   2. ]
#  [ 7.   6.   1. ]]
print(arr3)
# result:
# [[ 0.  0.  0.]
#  [ 0.  0.  0.]]
print(arr4)
# result:
# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]
print(arr5)
# result:
# [[ 0.31654004  0.87056375  0.29050563]
#  [ 0.55267505  0.59191276  0.20174988]]
print(arr6)
# result: [ 5  8 11 14 17]
print(arr7)
# result: [ 0.    0.25  0.5   0.75  1.    1.25  1.5   1.75  2.  ]
print('-'*70)



print('''访问数组''')

# 查看数组的属性
print(arr2.shape) # 返回矩阵的规格
# result: (2,3)
print(arr2.ndim)  # 返回矩阵的秩
# result: 2
print(arr2.size)  # 返回矩阵元素总数
# result: 6
print(arr2.dtype.name)   # 返回矩阵元素的数据类型
# result: float64
print(type(arr2)) # 查看整个数组对象的类型
# result： <type 'numpy.ndarray'>

# 通过索引和切片访问数组元素
def f(x,y):
    return 10*x+y
arr8 = np.fromfunction(f,(4,3),dtype = int)
print(arr8)
# result:
# [[ 0  1  2]
# [10 11 12]
# [20 21 22]
# [30 31 32]]
print(arr8[1,2]) #返回矩阵第1行，第2列的元素（注意下标从0开始）
# result: 12
print(arr8[0:2,:])  #切片，返回矩阵前2行
# result:
# [[ 0  1  2]
#  [10 11 12]]
print(arr8[:,1])    #切片，返回矩阵第1列
# result: [ 1 11 21 31]
print(arr8[-1])     #切片，返回矩阵最后一行
# reuslt: [30 31 32]

# 通过迭代器访问数组元素
for row in arr8:
    print(row)
# result:
# [0 1 2]
# [10 11 12]
# [20 21 22]
# [30 31 32]
for element in arr8.flat:
    print(element)
# 输出矩阵全部元素
print('-'*70)



print('''数组的运算''')
arr9 = np.array([[2,1],[1,2]])
arr10 = np.array([[1,2],[3,4]])
print(arr9 - arr10)  
# result:
# [[ 1 -1]
#  [-2 -2]]
print(arr9**2)
# result:
# [[4 1]
#  [1 4]]
print(3*arr10)
# result:
# [[ 3  6]
#  [ 9 12]]
print(arr9*arr10)  #普通乘法
# result：
# [[2 2]
#  [3 8]]
print(np.dot(arr9,arr10))  #矩阵乘法
# result:
# [[ 5  8]
#  [ 7 10]]
print(arr10.T)  #转置
# result:
# [[1 3]
#  [2 4]]
print(np.linalg.inv(arr10)) #返回逆矩阵
# result:
# [[-2.   1. ]
#  [ 1.5 -0.5]]
print(arr10.sum())  #数组元素求和
# result: 10
print(arr10.max())  #返回数组最大元素
# result: 4
print(arr10.cumsum(axis = 1))  #沿行累计总和
# result： 
# [[1 3]
#  [3 7]]
print('-'*70)



print('''NumPy通用函数''')
print(np.exp(arr9))     #指数函数
# result:
# [[ 7.3890561   2.71828183]
#  [ 2.71828183  7.3890561 ]]
print(np.sin(arr9))      #正弦函数（弧度制）
# result:
# [[ 0.90929743  0.84147098]
#  [ 0.84147098  0.90929743]]
print(np.sqrt(arr9))     #开方函数
# result:
# [[ 1.41421356  1.        ]
#  [ 1.          1.41421356]]
print(np.add(arr9,arr10))  #和arr9+arr10效果一样
# result:
# [[3 3]
#  [4 6]]
print('-'*70)



print('''数组合并与分割''')
# 合并
arr11 = np.vstack((arr9,arr10))  #纵向合并数组，由于与堆栈类似，故命名为vstack
print(arr11)
# result:
# [[2 1]
#  [1 2]
#  [1 2]
#  [3 4]]
arr12 = np.hstack((arr9,arr10))  #横向合并数组
print(arr12)
# result:
# [[2 1 1 2]
#  [1 2 3 4]]
# 分割
print(np.hsplit(arr12,2))  # 将数组横向分为2部分
# result:
# [array([[2, 1],
#        [1, 2]]), array([[1, 2],
#        [3, 4]])]
print(np.vsplit(arr11,2))   # 数组纵向分为2部分
# result:
# [array([[2, 1],
#        [1, 2]]), array([[1, 2],
#        [3, 4]])]
