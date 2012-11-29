from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_zlim(0, 10)

v = [
    (0,0,0),#0
    (3,0,0),#1
    (3,0,2),#2
    (0,0,2),#3
    (0,1,0),#4
    (3,1,0),#5
    (3,1,2),#6
    (0,1,2) #7
]
def draw_rectangular_prism(v):
    ax.add_collection3d(Poly3DCollection([v[:4]]))
    ax.add_collection3d(Poly3DCollection([v[4:]]))
    ax.add_collection3d(Poly3DCollection([[v[0], v[3], v[7], v[4]]]))
    ax.add_collection3d(Poly3DCollection([[v[0], v[4], v[5], v[1]]]))
    ax.add_collection3d(Poly3DCollection([[v[3], v[7], v[6], v[2]]]))
    ax.add_collection3d(Poly3DCollection([[v[1], v[5], v[6], v[2]]]))
    
draw_rectangular_prism(v)

plt.show()