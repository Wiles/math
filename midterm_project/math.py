import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update_line(num, data, line):
    line.set_data(data[...,:num])
    return line,
    
def do_points(interval, x_first_coef, x_second_coef,  y_first_coef, y_second_coef ):
    time = 0.0
    y = [];
    x = [];
    while True:
        next_y = (y_first_coef*time) + (y_second_coef * (time ** 2))
        if next_y < 0 and time != 0:
            break
        else:
            y.append(next_y)
            x.append((x_first_coef*time) + (x_second_coef * (time ** 2)))
            time += interval
    return x, y
    	
def do_math():

    plt.xlabel('Distance')
    plt.xlabel('Height')
    plt.title('Golf Ball Flight')
    
    distance_air, height_air = do_points(0.01, 32, -0.1, 42, -4.9)
    plt.plot(distance_air, height_air, label="w/ air")
    distance, height = do_points(0.01, 32, -0.0, 42, -4.9)
    plt.plot(distance, height, label="w/o air")
    plt.xlim(min(distance + distance_air), max(distance + distance_air) + 10)
    plt.ylim(min(height + height_air), max(height + height_air) + 10)
    
    plt.legend()
    plt.show()

if __name__ == "__main__":
	print do_math();