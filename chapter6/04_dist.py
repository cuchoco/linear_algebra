# 점 A를 포함하고 법선벡터가 W인 평면과 점 P 사이의 거리를 계산하라.
import numpy as np
A = np.array([2,3,4])
W = np.array([1,2,3])
P = np.array([0,1,2])

# |(P-A) dot W| / norm(W)

def distPt2Pl(A,W,P):
    num = np.dot((P-A).T, W)
    deno = np.linalg.norm(W)
    val = np.abs(num) / deno
    return val

print("거리: ", distPt2Pl(A, W, P))