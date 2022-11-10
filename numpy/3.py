import numpy as np

def catch(arr):
    locked = 0
    open = 1
    if arr[0] == 0: 
        return locked
    else: 
        for i in range(len(arr)):
            if arr[i] == open: 
                continue
            else: 
                if open == 1:
                    open = 0 
                else: 
                    open=1
                locked += 1

    return locked + 1

print(catch([1, 1, 0, 0, 0, 1, 0]))