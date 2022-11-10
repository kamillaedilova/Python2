import numpy as np

a = np.array([(1, 2, 3),(4, 5, 6), (7, 8, 9)])
print (a)
trans = a.T
def check():
    for i in range(len(trans)):
        for j in range(len(trans[i])-1):
            if trans[i][j] >= trans[i][j+1]:
                return False
    return True

print(check())