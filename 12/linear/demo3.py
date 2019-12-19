# 梯度下降求解线性分析模型参数

import numpy as np
from numpy.linalg import inv
from numpy import dot
from numpy import mat


# y=2x

x = mat([1,2,3]).reshape(3,1)
y = 2*x


#theta = theta -alpha*(theta*x-y)*x
theta = 1.
alpha = 0.1

for i in range(100):
	theta = theta+ np.sum(alpha * (y-dot(x,theta))*x.reshape(1,3))/3.

print('x\n',x)
print('y\n',y)
print('theta\n',theta)
