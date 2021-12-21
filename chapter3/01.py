import numpy as np
v1 = np.array([1,2,3])
v2 = np.array([4,5,6])
v3 = np.array([7,8,9])
c = np.array(
    [[1,2],
     [3,4],
     [5,6]]
)

d = np.column_stack((c,v3))

e = np.array(
    [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12]]
)

def ts(array):
    return np.transpose(array)

A = np.vstack((v1,v2,v3))
B = np.column_stack((v1,v2,v3))

print('A: \n', A)
print("B: \n", B)
print("D: \n", d)

print("e 부분행렬: \n", e[0,3], e[1,2], e[:2,2], e[0:2, 2:4], e[2,:])

e[0,0] = -1
print("e 성분바꾸기 \n", e)