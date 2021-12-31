import sys
sys.path.append('..')
from utils import pprint
import numpy as np

import numpy as np

def solveByCrammer(A, B):   # 크래머 공식을 이용한 Ax = B의 풀이
    x = np.zeros(len(B))
    C = np.copy(A)
    for i in range(0, len(B)):
        for j in range(0, len(B)):
            C[j, i] = B[j]
            if i > 0:
                C[j, i-1] = A[j, i-1]
        # pprint(f'C{i}', C)
        x[i] = np.linalg.det(C) / np.linalg.det(A)
    return x

A = np.array([
    [2,-1,5,1],
    [3,2,2,-6],
    [1,3,3,-1],
    [5,-2,-3,3]
])

B = np.array([[-3], [-32], [-47], [49]])

X = solveByCrammer(A, B)
print("X:", X)

A = np.array([[1,2,1],[2,2,1],[1,2,3]])
B = np.array([[5],[6],[9]])

X = solveByCrammer(A, B)
print("X:", X)