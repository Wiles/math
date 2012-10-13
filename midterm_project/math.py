import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
    
def do_points(interval, max_t, x_first_coef, x_second_coef,  y_first_coef, y_second_coef ):
    y = [];
    x = [];
    for time in np.arange(0, max_t, interval):
        y.append((y_first_coef*time) + (y_second_coef * (time ** 2)))
        x.append((x_first_coef*time) + (x_second_coef * (time ** 2)))
    return x, y
    	
def do_math(max_t):
    
    distance_air, height_air = do_points(0.001, max_t, 32, -0.1, 42, -4.9)
    plt.plot(distance_air, height_air, label="w/ air")
    distance, height = do_points(0.001, max_t, 32, -0.0, 42, -4.9)
    plt.plot(distance, height, label="w/o air")
    plt.xlim(min(distance + distance_air) - 10, max(distance + distance_air) + 10)
    plt.ylim(min(height + height_air) - 10, max(height + height_air) + 10)
    
    plt.xlabel('Distance')
    plt.xlabel('Height')
    plt.title('Golf Ball Flight')
    plt.grid(True)
    plt.legend()
    plt.show()

def do_quadratic(a, b, c):
    d = sqrt((b ** 2) - (4 * (a) * (c)))
    return (-b + (d))/(2*a), (-b - (d))/(2*a)        

if __name__ == "__main__":
	print do_math(max(do_quadratic(-4.9, 42, 0)));