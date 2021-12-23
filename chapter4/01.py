import sys
sys.path.append('..')
from utils import npr, pprint
import numpy as np

# 행렬 생성
np.random.seed(0)
A = npr([
    [1,2],
    [3,4]
])
B = np.random.rand(3,3)
C = npr([
    [5,3,2,1],
    [6,2,4,5],
    [7,4,1,3],
    [4,3,5,2]
])
D = npr([[4],[2],[5],[1]])

#---------------------------------
Ainv = np.linalg.inv(A)
I = np.matmul(A,Ainv)
pprint("A",A)
pprint("A @ Ainv", I)
#---------------------------------

#---------------------------------
Binv = np.linalg.inv(B)
I = np.matmul(B, Binv)
pprint("B", B)
pprint("B @ Binv", I)
#---------------------------------

#---------------------------------
Cinv = np.linalg.inv(C)
pprint("Cinv", Cinv)
x = np.matmul(Cinv, D)
pprint("x", x)
#---------------------------------
