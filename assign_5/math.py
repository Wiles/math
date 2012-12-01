from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.colors import colorConverter
import matplotlib.pyplot as plt
from texttable import *

cc = lambda arg: colorConverter.to_rgba(arg, alpha=1.0)

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

def draw_rectangular_prism(v, col):
    ax.add_collection3d(Poly3DCollection([v[:4]], facecolors = [cc(col)]))
    ax.add_collection3d(Poly3DCollection([v[4:]], facecolors = [cc(col)]))
    ax.add_collection3d(Poly3DCollection([[v[0], v[3], v[7], v[4]]], facecolors = [cc(col)]))
    ax.add_collection3d(Poly3DCollection([[v[0], v[4], v[5], v[1]]], facecolors = [cc(col)]))
    ax.add_collection3d(Poly3DCollection([[v[3], v[7], v[6], v[2]]], facecolors = [cc(col)]))
    ax.add_collection3d(Poly3DCollection([[v[1], v[5], v[6], v[2]]], facecolors = [cc(col)]))
    
def rotate_rectangular_prism(v, deg, vert):
    return v

def translate_rectangular_prism(v, x, y, z):
    return [[e[0] + x, e[1] + y, e[2] + z] for e in v]
    
def print_points(v):
	table = Texttable()
	table.set_precision(4)
	table.set_deco(Texttable.HEADER)
	table.header(["x", "y", "z"])
	table.set_cols_align([("r") for i in range(0, len(v[0]))])
	[(table.add_row(row)) for row in v]
	print table.draw()
    
draw_rectangular_prism(v, 'r')
print_points(v)
vv = translate_rectangular_prism(rotate_rectangular_prism(v, 60, 'z'), 2, 4, 1)
draw_rectangular_prism(vv, 'b')
print
print_points(vv)

plt.show()