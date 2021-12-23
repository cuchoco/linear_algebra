import numpy as np

def pprint(msg, A):
    print("---", msg, "---")
    (n, m) = A.shape
    for i in range(0,n):
        line = ""
        for j in range(0, m):
            line += "{0:.2f}".format(A[i,j]) + "\t"
        print(line)
    print("")


def npr(array):
    return np.array(array, dtype=np.float32)
