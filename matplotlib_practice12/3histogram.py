import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots()

days=['Mon','Tue','Wed','Thur','Fri','Sat','Sun']
colors=['Red','Orange','Yellow','Green','Cyan','Blue','Purple']
counts=[25,48,70, 8, 17,66, 28]

ax.bar(days, counts, color=colors)

ax.set_title('Weekday Data')

plt.show()
import matplotlib.pyplot as plt
import numpy as np

 

'''days =['Mon','Tue','Wed','Thur','Fri','Sat','Sun']
data = np.random.gamma(4, scale=0.2, size=1000)*110+1910
colors = ['aqua', 'red', 'gold', 'royalblue', 'darkorange', 'green', 'purple', 'cyan', 'yellow', 'lime']

 

fig, ax = plt.subplots(figsize=(8,4), facecolor='w')
cnts, values, bars = ax.hist(data, edgecolor='k', bins=days)
ax.set_xticks(days)

 

for i, (cnt, value, bar) in enumerate(zip(cnts, values, bars)):
    bar.set_facecolor(colors[i % len(colors)])
plt.show()'''