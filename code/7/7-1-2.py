# -*- coding:utf8 -*-
import pandas as pd
from sklearn.linear_model import LogisticRegression, RandomizedLogisticRegression
from sklearn.cross_validation import train_test_split

# 导入数据并观察
data = pd.read_csv('LogisticRegression.csv', encoding='utf-8')
# print data.head(5)    # 查看数据框的头五行

# 将类别型变量进行独热编码one-hot encoding
data_dum = pd.get_dummies(data, prefix='rank', columns=['rank'], drop_first=True)
print(data_dum.tail(5))    # 查看数据框的最后五行
# result:
#     admit  gre   gpa  rank_2  rank_3  rank_4
# 395      0  620  4.00     1.0     0.0     0.0
# 396      0  560  3.04     0.0     1.0     0.0
# 397      0  460  2.63     1.0     0.0     0.0
# 398      0  700  3.65     1.0     0.0     0.0
# 399      0  600  3.89     0.0     1.0     0.0

# 切分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(data_dum.ix[:, 1:], data_dum.ix[:, 0], test_size=.1, random_state=520)

lr = LogisticRegression()    # 建立LR模型
lr.fit(X_train, y_train)    # 用处理好的数据训练模型
print('逻辑回归的准确率为：{0:.2f}%'.format(lr.score(X_test, y_test) *100))
