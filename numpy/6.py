import numpy as np
from numpy import*
import array
arr=np.array([
  ["-", "-", "-", "-", "#"],
  ["-", "-", "-", "-", "-"],
  ["-", "-", "#", "-", "-"],
  ["-", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-"]
])
array1=np.array([
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0]
])
#print(arr)
n=5

for i in range (n):
    for j in range(n):
       array1[i][j]=int(array1[i,j])
       if arr[i][j]=="#" :
            array1[i][j]=arr[i][j]
            array1[i+1][j]=+1
            array1[i][j+1]=+1
            array1[i+1][j+1]=+1

            array1[i-1][j]=+1
            array1[i][j-1]=+1
            array1[i-1][j-1]=+1
            
            array1[i-1][j+1]=+1
            array1[i+1][j-1]=+1
          
            array1[i+1][j]=+1
            array1[i][j+1]=+1
            array1[i+1][j+1]=+1
            
print(array1)
