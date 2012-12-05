from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.colors import colorConverter
import matplotlib.pyplot as plt
from texttable import *
import math

cc = lambda arg: colorConverter.to_rgba(arg, alpha=1.0)

fig = plt.figure()
ax = Axes3D(fig)

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_zlim(0, 10)


plt.xlabel('X')
plt.ylabel('Y')

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

def do_math(deg, v, x, y, z):
    vv = []
    matrix = [
        [math.cos(math.radians(60.0)), -math.sin(math.radians(60.0)), 0, x],
        [math.sin(math.radians(60.0)), math.cos(math.radians(60.0)), 0, y],
        [0,0,1,z],
        [0,0,0,1]
    ]
    
    for vector in v:
        vv.append([
            vector[0] * matrix[0][0] + vector[1] * matrix[0][1] + vector[2] * matrix[0][2] + 1 * matrix[0][3],
            vector[0] * matrix[1][0] + vector[1] * matrix[1][1] + vector[2] * matrix[1][2] + 1 * matrix[1][3],
            vector[0] * matrix[2][0] + vector[1] * matrix[2][1] + vector[2] * matrix[2][2] + 1 * matrix[2][3]
        ])
    return vv
    
def print_points(v):
	table = Texttable()
	table.set_precision(4)
	table.set_deco(Texttable.HEADER)
	table.set_cols_dtype(['f', 'f', 'f'])
	table.header(["x", "y", "z"])
	table.set_cols_align([("r") for i in range(0, len(v[0]))])
	[(table.add_row(row)) for row in v]
	print table.draw()
    
draw_rectangular_prism(v, 'r')
print_points(v)
vv = do_math(60.0, v, 2, 4, 1)
draw_rectangular_prism(vv, 'b')
print
print_points(vv)

plt.show()