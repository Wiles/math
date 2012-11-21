import numpy as np
import math
from texttable import *
import sys

table = Texttable()
table.set_precision(6)
table.set_deco(Texttable.HEADER)
table.header(["x", "y"])
table.set_cols_dtype(['t', 'f'])
    
def trapezoidal_rule(y, start, end, intervals):
    height = (end - start) / intervals
    total = y(start) + y(end)
    table.add_row(["{0:.2f}".format(start), y(start)])
    for i in xrange(1, intervals):
        point = start + i * height
        table.add_row(["{0:.2f}".format(point), y(point)])
        total += 2 * y(point)
    table.add_row(["{0:.2f}".format(end), y(end)])
    return total * height / 2

if __name__ == "__main__":
    n = int(sys.argv[1])
    print "n = " + str(n)
    at = trapezoidal_rule(lambda x: (math.sqrt(x ** 2 + 4)), 0.0, 1.0, n)

    #print table.draw()

    def area(x, a):
        return ((x/2) * math.sqrt(x **2 + a ** 2)) + (((a ** 2)/2) * math.log(x + math.sqrt(x ** 2 + a ** 2)))
    print
    area = area(1.0, 2.0) - area(0.0, 2.0)
    print "area = {0:.6f}".format(area)
    print "at   = {0:.6f}".format(at)
    print "dev  = {0:.2e}".format((at - area)/area)