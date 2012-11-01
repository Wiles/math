import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

def get_y(x, m, rc, b):
	return math.exp(b) * (math.e ** ( - x/rc))
	
def get_ys(x, m, rc, b):
	return [get_y(_x, m,rc, b) for _x in x]
	
def sq_sum(x_in):
	return sum([x_out ** 2 for x_out in x_in])
	
def ln(l):
	return [math.log(x) for x in l]
	
def diff(y1, y2):
	return [y1[i] - y2[i] for i in range(len(y1))]
	
x = [2.0,4.0,6.0,8.0,10.0,12.0, 14.0,16.0,18.0,20.0,22.0,24.0,26.0,28.0,30.0]
y = [9.7,8.1,6.6,5.1,4.4,3.7,2.8,2.4,2.0,1.6,1.4,1.1,0.85,0.69,0.6]

n = len(x)
X = x
Y = ln(y)

xy = [x[i] * y[i] for i in range(n)]
XY = [X[i] * Y[i] for i in range(n)]
m = (n * sum(XY) - (sum(X) * sum(Y)))/((n * sq_sum(X))-(sum(X) ** 2))
rc = -1 /m
b = ((sq_sum(X)) * (sum(Y)) - (sum(XY) * sum(X)))/((n * sq_sum(X))-(sum(X) ** 2))

error = sq_sum(diff(y, get_ys(X, m, rc, b)))


fig = plt.figure()
ax = fig.add_subplot(111)

plt.xlim(min(x) - 1, max(x) + 1)
plt.ylim(min(y) - 1, max(y) + 1)

a, = ax.plot(x, y, linestyle='none', marker='.')

xes = np.arange(min(x), max(x), 0.01)

a, = ax.plot(xes, get_ys(xes, m, rc, b))

plt.xlabel('Time (s)')
plt.ylabel('Voltage (v)')
plt.title('Non-linear Curve Fitting')

plt.annotate('E = ' + "%0.5f" % math.exp(b), xy=(min(x), min(y) + 2))
plt.annotate('rc = ' + "%0.5f" % rc, xy=(min(x), min(y) + 1))
plt.annotate('error = ' + "%0.5f" % error, xy=(min(x), min(y)))

plt.show()