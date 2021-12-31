import sys

from numpy.core.getlimits import _register_type
from numpy.linalg.linalg import det
sys.path.append('..')
from utils import pprint
import numpy as np

def cofactor(A, i, j):    # 여인수 계산
    (n,m) = A.shape
    # 소행렬 생성
    M = np.zeros((n-1, m-1))
    for a in range(0, n-1):
        k = a if (a < i) else a+1
        for b in range(0, m-1):
            l = b if (b < j) else b+1
            M[a, b] = A[k,l]
    # a(ij) 소행렬식(minordet) * (-1)**i+j = a(ij) 의 여인수
    cofactor = (-1)**(i+j)*np.linalg.det(M)
    return cofactor

def inverseByAdjointMatrix(A):    # 수반행렬을 이용한 A의 역행렬 계산
    detA = np.linalg.det(A)
    (n, m) = A.shape
    adjA = np.zeros((n,m))

    # 수반행렬 생성
    for i in range(0, n):        
        for j in range(0, m):
            adjA[j, i] = cofactor(A, i, j)
    

    # A 역행렬 = 1/det(A) * adj A
    if detA != 0.0:
        return (1./detA) * adjA
    else:
        return 0


A = np.array([
    [-4,0,2,-1,0],
    [1,3,-3,-1,4],
    [2,0,1,3,0],
    [-2,1,-3,-1,5],
    [1,-5,1,0,5]
])

Ainv = inverseByAdjointMatrix(A)

pprint("A ", A)
pprint("A inverse", Ainv)