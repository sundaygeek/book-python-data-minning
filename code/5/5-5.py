from sklearn import datasets

print('''加载数据集''')

# 数据集类似字典对象，包括了所有的数据和关于数据的元数据（metadata）。
# 数据被存储在.data成员内，是一个n_samples*n_features的数组。
# 在有监督问题的情形下，一个或多个因变量（response variables）被储存在.target成员中

digits = datasets.load_digits()

# 例如在digits数据集中，digits.data是可以用来分类数字样本的特征
print(digits.data)
# result:
# [[  0.   0.   5. ...,   0.   0.   0.]
#  [  0.   0.   0. ...,  10.   0.   0.]
#  [  0.   0.   0. ...,  16.   9.   0.]
#  ..., 
#  [  0.   0.   1. ...,   6.   0.   0.]
#  [  0.   0.   2. ...,  12.   0.   0.]
#  [  0.   0.  10. ...,  12.   1.   0.]]


# digits.target给出了digits数据集的目标变量，即每个数字图案对应的我们想预测的真是数字
print(digits.target)
# result:
# [0 1 2 ..., 8 9 8]



print('''训练和预测''')

from sklearn import svm

# 选择模型参数
clf = svm.SVC(gamma=0.0001,C=100)

# 我们的预测器的名字叫做clf。现在clf必须通过fit方法来从模型中学习。
# 这个过程是通过将训练集传递给fit方法来实现的。我们将除了最后一个样本的数据全部作为训练集。

# 进行训练
clf.fit(digits.data[:-1], digits.target[:-1])

# 进行预测
print(clf.predict(digits.data[-1].reshape(1, -1)))
# result: 8
