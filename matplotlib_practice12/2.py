#3 circles
import matplotlib.pyplot as plt

figure, axes = plt.subplots()
c1 = plt.Circle( (0, 0 ),10 ,fill = False )
c2 = plt.Circle( (0, 40 ),50 ,fill = False )
c3 = plt.Circle( (0, 90 ),100 ,fill = False )
plt.xlim([-200,200])
plt.ylim([-50,200])
axes.set_aspect( 1 )
axes.add_artist( c1 )
axes.add_artist( c2 )
axes.add_artist( c3 )
plt.title( 'Circles' )
plt.show()