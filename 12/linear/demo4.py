# 线性回归模型分析
import numpy as np
from numpy.linalg import inv
from numpy import dot
from numpy import mat
import pandas as pd

dataset = pd.read_csv('data.csv')

temp = dataset.iloc[:,2:5]
temp['x0'] = 1
x = temp.iloc[:,[3,0,1,2]]
# print(x)
y = dataset.iloc[:,1]
# print(y)

# 方法1-向量法
# theta = dot(dot(inv(dot(x.T,x)),x.T),y)
# print(theta.reshape(4,1))

# 方法2-梯度下降
# theta = np.array([1.,1.,1.,1.]).reshape(4,1)
# alpha = 0.1
# te = theta
# x0 = x.iloc[:,0].values.reshape(150,1)
# x1 = x.iloc[:,1].values.reshape(150,1)
# x2 = x.iloc[:,2].values.reshape(150,1)
# x3 = x.iloc[:,3].values.reshape(150,1)
# y = y.values.reshape(150,1)

# for i in range(10000):
# 	te[0] = theta[0]+alpha*np.sum((y-dot(x,theta))*x0)/150.
# 	te[1] = theta[1]+alpha*np.sum((y-dot(x,theta))*x1)/150.
# 	te[2] = theta[2]+alpha*np.sum((y-dot(x,theta))*x2)/150.
# 	te[3] = theta[3]+alpha*np.sum((y-dot(x,theta))*x3)/150.
# 	theta = te

# print(theta)
