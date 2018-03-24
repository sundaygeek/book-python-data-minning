# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x**2)

plt.figure(figsize=(8,4))
plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
plt.plot(x,z,"b--",label="$cos(x^2)$")
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("PyPlot First Example")
plt.ylim(-1.2,1.2)
plt.legend()
plt.show()



# -*- coding:utf-8 -*-
import matplotlib.pylab as plt
import numpy as np
# 第一部分
plt.subplot(2,1,1)    # 参数依次为：行，列，第几项
# 第二部分
plt.subplot(2,2,3)
# 第三部分
plt.subplot(2,2,4)
plt.show()



# -*- coding:utf-8 -*-
import matplotlib.pylab as plt
import numpy as np
# 第一部分
plt.subplot(2,1,1)    # 参数依次为：行，列，第几项
n = 12
X = np.arange(n)
Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
Y2 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)

# 利用plt.bar(x, y)绘制柱状图，并指定柱状图颜色，柱子边框颜色
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x, y in zip(X,Y1):
    # 利用plt.text()指定文字出现的坐标和内容
    plt.text(x+0.4, y+0.05, '%.2f' % y, ha='center', va='bottom')

# 利用plt.ylim(y1, y2)限制图形打印时对应的纵坐标范围
plt.ylim(-1.25,+1.25)


# 第二部分
plt.subplot(2,2,3)
n = 20
Z = np.random.uniform(0,1,n)
plt.pie(Z)

# 第三部分
plt.subplot(2,2,4)
X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
Y_C, Y_S = np.cos(X), np.sin(X)

plt.plot(X, Y_C, color="blue", linewidth=2.5, linestyle="-")
plt.plot(X, Y_S, color="red", linewidth=2.5, linestyle="-")

plt.xlim(X.min()*1.1, X.max()*1.1)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

plt.ylim(Y_C.min()*1.1, Y_C.max()*1.1)
plt.yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])
plt.show()

