import sys
from texttable import *

def do_math(kMin, kMax, x):
	table = Texttable()
	table.set_cols_dtype(['i', 'f', 'e'])
	table.header(["k", "approximation", "deviation"])
	table.set_precision(6)
	
	actual = 2/(2-x)
	estimation = 0
	for i in range(0, kMax + 1):
		estimation += (x/2) ** i
		if i >= kMin:
			table.add_row([i, estimation, ((estimation - actual)/actual)])
			
	print "x = %s" % (x)
	print table.draw()
	print
		
if __name__ == "__main__":
	for arg in sys.argv[1:]:
		do_math(4, 7, float(arg))