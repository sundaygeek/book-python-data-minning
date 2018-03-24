print('''改变工作目录''')
import os
os.chdir('/home/zh/')  # 改变路径至F盘的Data文件夹下，注意不是反斜杠
print(os.getcwd())
# result: F:\Data
print('-'*70)


print('''文件读写''')
data=[]  # 先定义存储数据的总列表，总列表的每个元素都是一个列表，各存储一行数据
fr = open('../data/ticdata.txt')# 打开文件
for line in fr.readlines():  # r eadlines()返回的是一个字符串列表，每个字符串代表一行原始数据
    line = line.strip()   # 去掉换行符
    data_line = line.split('\t') # 通过字符串的制表符\t分隔数据，并且返回一个列表，使用列表存储该行数据
    data.append(data_line)      # 将存储一行数据的列表添加到总列表中
print(data[0])  # 输出第一行的数据
fr.close()
print('-'*70)



print('''文件读写''')
f = open('output.txt','w')
# 使用join方法和write方法
data=[['1','2'],['3','4']]
line1 = ','.join(data[0])
f.write(line1+'\n')
line2 =','.join(data[1])
f.write(line2+'\n')
# 使用print>>f,
data=[[1,2],[3,4]]
for line in data:
    print(str(line[0])+','+str(line[1])+'\n', end=' ', file=f)
f.close()
print('-'*70)


print('''使用json处理数据''')
import json
# 使用dumps()和loads()
x=dict(height=176,weight=60)
print('原始字典内容：',x)
y = json.dumps(x) # 返回字符串
print('序列化后的字典：',y)
x = json.loads(y)
print('反序列化后又还原为原始的字典：',x)

# 使用dump()和load()
f=open('../tmp/BigData.json','w')
json.dump(x,f) # 保存到文件中
f.close()

f=open('../tmp/BigData.json','r')
print('从文件读取到的json：',json.load(f)) 
f.close()