import numpy as np
import matplotlib.pyplot as plt
import math
	
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

get_y = lambda x: (math.exp(b) * (math.e ** ( - x/rc)))
get_ys = lambda xes: [get_y(x) for x in xes]

yes = get_ys(X)
error = sq_sum(diff(y, yes))

fig = plt.figure()
ax = fig.add_subplot(111)

plt.xlim(min(x) - 1, max(x) + 1)
plt.ylim(min(y) - 1, max(y) + 1)

a, = ax.plot(x, y, linestyle='none', marker='.')

xes = np.arange(min(x), max(x), 0.01)
if max(x) != max(xes):
	xes = np.append(xes, [max(x)])

a, = ax.plot(xes, get_ys(xes))

plt.xlabel('Time (s)')
plt.ylabel('Voltage (v)')
plt.title('Non-linear Curve Fitting')

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in xrange(1, n):
        s += 2 * f(a + i * h)
    return s * h / 2
	
def simpson(f, a, b, n):
    h = float(b - a) / n
    S = f(a)
 
    for i in range(1, n, 2):
        x = a + h * i
        S += 4 * f(x)
 
    for i in range(2, n-1, 2):
        x = a + h * i
        S += 2 * f(x)
 
    S += f(b)
    F = h * S / 3
 
    return F

plt.annotate('AS = ' + "%0.5f" % simpson(get_y, min(x), max(x), 1000), xy=(min(x), min(y) + 4))
plt.annotate('AT = ' + "%0.5f" % trapezoidal_rule(get_y, min(x), max(x), 1000), xy=(min(x), min(y) + 3))
plt.annotate('E = ' + "%0.5f" % math.exp(b), xy=(min(x), min(y) + 2))
plt.annotate('rc = ' + "%0.5f" % rc, xy=(min(x), min(y) + 1))
plt.annotate('error = ' + "%0.5f" % error, xy=(min(x), min(y)))

plt.show()