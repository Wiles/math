import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

def get_y(x, m, b):
	return m * x + b
	
def get_ys(x, m, b):
	return [get_y(_x, m, b) for _x in x]
	
def sq_sum(x_in):
	return sum([x_out ** 2 for x_out in x_in])
	
def diff(y1, y2):
	return [y1[i] - y2[i] for i in range(len(y1))]
	
x = [8.0,2.0,11.0,6.0,5.0,4.0,12.0,9.0,6.0,1.0]
y = [3.0,10.0,3.0,6.0,8.0,12.0,1.0,4.0,9.0,14.0]

n = len(x)
xy = [x[i] * y[i] for i in range(n)]
x_square = [x[i] ** 2 for i in range(n)]

m = (sum(xy)-((sum(x)*sum(y))/n))/(sum(x_square)-(sum(x)**2/(n)))
b = (sum(y)/n)-m * (sum(x)/n)

plt.xlim(0, 15)
plt.ylim(0, 15)

r = ((n * (sum(xy))) - (sum(x) * sum(y))) / (math.sqrt((n * sq_sum(x)) - (sum(x) ** 2)) * math.sqrt((n * sq_sum(y)) - (sum(y) ** 2)))
print r
error = sq_sum(diff(y, get_ys(x, m, b)))
print error

a, = plt.plot(x, y, linestyle='none', marker='.')
a, = plt.plot([0,15], [get_y(0, m, b), get_y(15, m, b)])
plt.show()