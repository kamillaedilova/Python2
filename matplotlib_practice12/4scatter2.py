#scatter
import numpy as np
import numpy.random
import matplotlib.pyplot as plt

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii
plt.ylim(-0.2, 1.2)
plt.xlim(-0.2,1.2)
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()