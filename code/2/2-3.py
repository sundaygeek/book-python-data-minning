print("布尔表达式")
print(True,False)
# result: True,False
print(True == 1)
# result: True
print(True + 2)
# result: 3
print(True + False*3)
# result: 1
print(3 > 2)
# result :True
print((1 < 3)*10)
# reuslt: 10
print('-'*70)



print("条件分支")
# 例1 判断天气
weather = 'sunny'
if weather =='sunny':
    print("shopping")
elif weather =='cloudy':
    print("playing football")
else:
    print("learning python")
# result: shopping
    
# 例2 选择两个数的较大者
import math
a = math.pi
b = math.sqrt(9.5)
if a>b:
    print(a)
else:
    print(b)
# result: 3.14159265359
# 例3 3个数简单排序
first = 1
second = 2
third = 3
if second<third:
    t = second
    second = third
    third = t
if first<second:
    t = first
    first = second
    second = t
if second<third:
    t = second
    second = third
    third = t
print(first,'>',second,'>',third)
#result: 3 > 2 > 1
print('-'*70)



print('''while循环''')
# 例1 1到1000求和
a = 1000
s = 0
while a:
    s+=a
    a-=1
print(s)
# result: 500500

# 例2 简单计算
while True:
    s = eval(input('1+2='))
    if s ==3:
        print('答案正确')
        break
    if s>=0 and s<=9:
        continue
    print('答案是个位数')

print('-'*70)



print('''简单for循环''')
# 对列表和字符串进行迭代
for a in ['e','f','g']:
    print(a, end=' ')
# result:e f g
print()
for a in 'string':
    print(a, end=' ')
# result：s t r i n g
print()
print('-'*70)



print('''range()函数''')
print(list(range(2,9)))
# result: [2, 3, 4, 5, 6, 7, 8]
print(list(range(2,9,3)))  # 相邻元素的间隔为3
# result: [2, 5, 8]
print('-'*70)

# 直接使用for循环难以改变序列元素
L = [1,2,3]
for a in L:
    a+=1  # a不是引用，L中对应的元素没有发生改变
print(L)  
# resukt: [1,2,3]

# range()与len()函数遍历序列并修改元素
for i in range(len(L)):
    L[i]+=1  # 通过索引访问
print(L) 
# result: [2,3,4]
print('-'*70)



print('''循环中的else语句''')
# 简单搜索质数
for n in range(2,10):
    for x in range(2,n):
        if n%x ==0:# 含有非普通因子
            print(n,'equals',x,'*',n/x)
            break
    else:
        print(n,'是一个质数')# 仅含有普通因子，说明这是一个质数
        


