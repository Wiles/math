import pylab as plt
import numpy as np
from matplotlib.widgets import Slider
from math import sqrt
    
def do_points(interval, max_t, x_first_coef, x_second_coef,  y_first_coef, y_second_coef ):
    y = [];
    x = [];
    for time in np.arange(0, max_t, interval):
        y.append((y_first_coef*time) + (y_second_coef * (time ** 2)))
        x.append((x_first_coef*time) + (x_second_coef * (time ** 2)))
        
    y.append((y_first_coef*max_t) + (y_second_coef * (max_t ** 2)))
    x.append((x_first_coef*max_t) + (x_second_coef * (max_t ** 2)))
    return x, y
 	
def do_math(interval, max_t, x_first_coef, x_second_coef,  y_first_coef, y_second_coef ):
    distance_air, height_air = do_points(interval, max_t, x_first_coef, x_second_coef,  y_first_coef, y_second_coef )
    a.set_xdata(distance_air)
    a.set_ydata(height_air)
    distance, height = do_points(interval, max_t, x_first_coef, 0.0,  y_first_coef, y_second_coef )
    b.set_xdata(distance)
    b.set_ydata(height)
    plt.draw()
    
def do_quadratic(a, b, c):
    d = sqrt((b ** 2) - (4 * (a) * (c)))
    return (-b + (d))/(2*a), (-b - (d))/(2*a)
    
def update(val):
    do_math(interval, val, ab, bb, cb, db)

ab = 32.0
bb = -0.1
cb = 42.0
db = -4.9
interval = 0.01

plt.subplot(111)

a, = plt.plot([], [], label="w/ air")
b, = plt.plot([], [], label="w/o air")
plt.xlim(-10, 300)
plt.ylim(-10, 300)

plt.xlabel('Distance')
plt.xlabel('Height')
plt.title('Golf Ball Flight')
plt.grid(True)
plt.legend()
max_time = max(do_quadratic(db, cb, 0))
distance_air, height_air = do_points(interval, max_time, ab, bb,  cb, db )
distance, height = do_points(interval, max_time, ab, 0.0,  cb, db )
plt.xlim(min(distance + distance_air) - 10, max(distance + distance_air) + 10)
plt.ylim(min(height + height_air) - 10, max(height + height_air) + 10)
do_math(interval, max_time, ab, bb, cb, db)
ax = plt.axes([0.125, 0.02, 0.775, 0.03], axisbg='lightgoldenrodyellow')
slider = Slider(ax, 'Time', 0, max_time, valinit=max_time)
slider.on_changed(update)
plt.show()
