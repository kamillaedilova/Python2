from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

color = plt.get_cmap('viridis')

fig = plt.figure()
ax = plt.axes(projection = '3d')

y=np.random.randint(-1000,1000,500)
x=np.random.randint(1000,4000,500)
z=np.random.randint(-1000,1000,500)

scatter = ax.scatter3D(x, y, z, c=x, cmap = color)
plt.colorbar(scatter)
plt.show()