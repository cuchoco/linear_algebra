import sys
sys.path.append('..')
from utils import npr, pprint

import numpy as np


A = npr([[1,2],[3,4]])
B = npr([[2,2],[1,3]])
C = npr([[4,5,6],[7,8,9]])
v = npr([[10],[20]])

d11 = npr([[1,2],[3,4]])
d12 = npr([[5],[6]])
d21 = npr([7,7])
d22 = npr([8])


pprint("A+B", A+B)
pprint("AB", np.matmul(A,B))

# 성분별 나눗셈, 곱셈
pprint("A/B", A/B)
pprint("A*B", A*B)

# 거듭제곱
pprint("A**2", np.linalg.matrix_power(A,2))

#Transpose
pprint("vT", np.transpose(v))

#블록행렬
pprint("block D", np.block([[d11,d12], [d21,d22]]))