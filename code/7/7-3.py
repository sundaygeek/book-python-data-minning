# BP神经网络Python实现

import numpy as np
from numpy import random
import math
import copy
import sklearn.datasets
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt

# 获取数据并分为训练集与测试集
trainingSet, trainingLabels = sklearn.datasets.make_moons(400, noise=0.20)
plt.scatter(trainingSet[trainingLabels==1][:,0], trainingSet[trainingLabels==1][:,1], s=40, c='r', marker='x',cmap=plt.cm.Spectral)
plt.scatter(trainingSet[trainingLabels==0][:,0], trainingSet[trainingLabels==0][:,1], s=40, c='y', marker='+',cmap=plt.cm.Spectral)
plt.show()
testSet = trainingSet[320:]
testLabels = trainingLabels[320:]
trainingSet = trainingSet[:320]
trainingLabels = trainingLabels[:320]

# 设置网络参数
layer =[2,3,1] # 设置层数和节点数
Lambda = 0.005 # 正则化系数
alpha = 0.2 # 学习速率
num_passes = 10000 # 迭代次数
m = len(trainingSet) # 样本数量

# 建立网络
# 网络采用列表存储每层的网络结构,网络的层数和各层节点数都可以自由设定
b = [] # 偏置元,共layer-1个元素,b[0]代表第一个隐藏层的偏置元(向量形式)
W = []
for i in range(len(layer)-1):
    W.append(random.random(size = (layer[i+1],layer[i]))) # W[i]表示网络第i层到第i+1层的转移矩阵(NumPy数组),输入层是第0层
    b.append(np.array([0.1]*layer[i+1]))  # 偏置元,b[i]的规模是1*第i+1个隐藏层节点数
a = [np.array(0)]*(len(W)+1) # a[0] = x,即输入,a[1]=f(z[0]),a[len(W)+1] = 最终输出
z = [np.array(0)]*len(W) # 注意z[0]表示是网络输入层的输出，即未被激活的第一个隐藏层

W = np.array(W)

def costfunction(predict,labels):
    # 不加入正则化项的代价函数
    # 输入参数格式为numpy的向量
    return sum((predict - labels)**2)
def error_rate(predict,labels):
    # 计算错误率,针对二分类问题,分类标签为0或1
    # 输入参数格式为numpy的向量
    error =0.0
    for i in range(len(predict)):
        predict[i] = round(predict[i]) 
        if predict[i]!=labels[i]:
            error+=1
    return error/len(predict)
def sigmoid(z):  # 激活函数sigmoid
    return 1/(1+np.exp(-z))
def diff_sigmoid(z): # 激活函数sigmoid的导数
    return sigmoid(z)*(1-sigmoid(z))

activation_function = sigmoid  # 设置激活函数
diff_activation_function = diff_sigmoid # 设置激活函数的导数


# 开始训练BP神经网络
a[0] = np.array(trainingSet).T # 改一列为一个样本，一行代表一个特征
y = np.array(trainingLabels)

for v in range(num_passes):
    # 前向传播
    for i in range(len(W)):
        z[i] = np.dot(W[i],a[i])
        for j in range(m):
            z[i][:,j]+=b[i] # 加上偏置元
        a[i+1] = activation_function(z[i]) # 激活节点

    predict = a[-1][0] # a[-1]是输出层的结果,即为预测值

    # 反向传播
    delta = [np.array(0)]*len(W) # delta[0]是第一个隐藏层的残差，delta[-1]是输出层的残差

    # 计算输出层的残差
    delta[-1] = -(y-a[-1])*diff_activation_function(z[-1])

    # 计算第二层起除输出层外的残差
    for i in range(len(delta)-1):
        delta[-i-2] = np.dot(W[-i-1].T,delta[-i-1])*diff_activation_function(z[-i-2]) # 这里是倒序遍历
        # 设下标-i-2代表第L层，则W[-i-1]是第L层到L+1层的转移矩阵，delta[-i-1]是第L+1层的残差，而z[-i-2]是未激活的第L层

    # 计算最终需要的偏导数值
    delta_w = [np.array(0)]*len(W)
    delta_b = [np.array(0)]*len(W)
    for i in range(len(W)):
        # 使用矩阵运算简化公式,下面2行代码已将全部样本反向传播得到的偏导数值求和
        delta_w[i] = np.dot(delta[i],a[i].T) 
        delta_b[i] = np.sum(delta[i],axis=1) 

    # 更新权重参数
    for i in range(len(W)):
        W[i] -= alpha*(Lambda*W[i]+delta_w[i]/m)
        b[i] -= alpha/m*delta_b[i]
  
print('训练样本的未正则化代代函数值:',costfunction(predict,np.array(trainingLabels)))  
print('训练样本错误率:',error_rate(predict,np.array(trainingLabels))) 

# 使用测试集测试网络
a[0] = np.array(testSet).T # 改一列为一个样本，一行代表一个特征
# 前向传播
m = len(testSet)
for i in range(len(W)):
    z[i] = np.dot(W[i],a[i])
    for j in range(m):
        z[i][:,j]+=b[i].T[0]
    a[i+1] = activation_function(z[i])
predict = a[-1][0]

print('测试样本的未正则化代代函数值:',costfunction(predict,np.array(testLabels)))
print('测试样本错误率:',error_rate(predict,np.array(testLabels)))
