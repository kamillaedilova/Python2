import matplotlib.pyplot as plt
import numpy as np

'''a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))'''
x = np.linspace(-1, 1, 100)
y = x**2 
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()