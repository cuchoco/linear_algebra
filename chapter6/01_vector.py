# 30도 방향으로 100의 힘
# 60도 방향으로 120의 힘

import numpy as np

def getVector(mag, deg): # 주어진 크기와 방향에 대응하는 벡터 생성
    vec = np.zeros(2)
    vec[0] = mag*np.cos(deg*2*np.pi/360)
    vec[1] = mag*np.sin(deg*2*np.pi/360)
    return vec

def getMagDeg(vec): # 벡터의 크기와 방향 계산
    mag = np.sqrt(vec[0]*vec[0] + vec[1]*vec[1])
    deg = np.arctan(vec[1]/vec[0]) * 360/(2*np.pi)
    return mag, deg

F1 = getVector(100, 30)
F2 = getVector(120, 60)
Fsum = F1 + F2
magn, angle = getMagDeg(Fsum)

print("결합한 힘의 크기: ", magn)
print("결합한 힘의 방향: ", angle)