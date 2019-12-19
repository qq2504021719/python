import numpy as np
from numpy.linalg import inv
from numpy import dot
from numpy import mat

a = np.mat([1,1])
print('a:\n',a)
print('a.reshape(2,1):\n',a.reshape(2,1))

b = mat([[1,2],[3,4]])
print('b:\n',b)
print('b的逆:\n',inv(b))
print('b.reshape(1,4):\n',b.reshape(1,4))

# a 1行2列  b是2行2列
print('a*b\n',dot(a,b))
