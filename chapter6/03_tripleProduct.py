# 네점 A,B,C,D에 대해 선분 AB,AC,AD로 만들어지는 평행육면체의 부피를 구하라
# 스칼라 삼중적의 절대값 = 평행 육면체의 부피
# AB dot (AC X AD)
import numpy as np

def tripleProduct(u, v, w):
    M = np.zeros((3,3))
    M[0:] = u
    M[1:] = v
    M[2:] = w
    val = np.linalg.det(M) # 행벡터가 u,v,w,인 행렬의 행렬식 계산
    return val

A = np.array([1,2,3])
B = np.array([0,5,2])
C = np.array([2,2,4])
D = np.array([2,4,1])

AB = B - A
AC = C - A
AD = D - A

val = tripleProduct(AB, AC, AD)
print("부피: ", np.abs(val))