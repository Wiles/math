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
	
x = [2.0,4.0,6.0,8.0,10.0,12.0, 14.0,16.0,18.0,20.0,22.0,24.0,26.0,28.0,30.0]
y = [9.7,8.1,6.6,5.1,4.4,3.7,2.8,2.4,2.0,1.6,1.4,1.1,0.85,0.69,0.6]

n = len(x)
xy = [x[i] * y[i] for i in range(n)]
x_square = [x[i] ** 2 for i in range(n)]

m = (sum(xy)-((sum(x)*sum(y))/n))/(sum(x_square)-(sum(x)**2/(n)))
b = (sum(y)/n)-m * (sum(x)/n)

plt.xlim(min(x) - 1, max(x) + 1)
plt.ylim(min(y) - 1, max(y) + 1)

r = ((n * (sum(xy))) - (sum(x) * sum(y))) / (math.sqrt((n * sq_sum(x)) - (sum(x) ** 2)) * math.sqrt((n * sq_sum(y)) - (sum(y) ** 2)))
print 'r = ' + str(r)
error = sq_sum(diff(y, get_ys(x, m, b)))
print 'e = ' + str(error)
print 'y = ' + str(m) + 'x+' + str(b)

a, = plt.plot(x, y, linestyle='none', marker='.')

xes = np.arange(min(x) - 1, max(x) + 1, 0.01)

a, = plt.plot(xes, get_ys(xes, m, b))
plt.show()