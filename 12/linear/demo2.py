# 最小二乘法

import numpy as np
from numpy.linalg import inv
from numpy import dot
from numpy import mat


# y=2x

x = mat([1,2,3]).reshape(3,1)
y = 2*x


# 二乘法算法theta = 点乘(点乘(求逆(点乘(x转质,x)),x转质),y)
theta = dot(dot(inv(dot(x.T,x)),x.T),y)
print('x\n',x)
print('y\n',y)
print('theta\n',theta)


