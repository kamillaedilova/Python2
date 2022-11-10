import numpy as np
import array as arr

array=np.array([(2, 2, 3, 6 ),(4, 5, 6, 15),(7, 8, 9, 24),(12,15,18,45)])
n=4
wr_num_row=[]
wr_num_col=[]

for i in range(n):
    summ=np.sum(array[i][:n-1])
    if summ!=array[i][n-1]:
        wr_num_row.append(i)
trans=array.transpose()
for i in range(n):
    summ2=np.sum(trans[i][:n-1])
    if summ2!=trans[i][n-1]:
        wr_num_col.append(i)
#print(wr_num_col)
for i in range(len(wr_num_row)):
    if wr_num_col[i] == n-1:
        ans = 0
        for j in range(n-1):
            ans += array[wr_num_row[i]][j]
    else:
        ans = array[wr_num_col[i]][n-1]
        for j in range(n-2, 0, -1):
            ans -= array[wr_num_row[i]][j]

    print(f"wrong number(arr{wr_num_row[i]+1}) -- {ans}")        

