import sys
from texttable import *

def file_to_matrix(file):
	return [([(float(x)) for x in line.split()]) for line in open(file).readlines()]

def print_matrix(matrix):
	table = Texttable()
	table.set_precision(1)
	table.set_deco(Texttable.HEADER)
	table.set_cols_align([("r") for i in range(0, len(matrix[0]))])
	[(table.add_row(row)) for row in matrix]
	print table.draw()

def do_math(matrix):
	for x in range(len(matrix)):
		matrix[x] = [(z / matrix[x][x]) for z in matrix[x]]
		for y in range(len(matrix)):
			if x == y:
				continue
			matrix[y] = [(matrix[y][z] - matrix[x][z] * matrix[y][x]) for z in range(len(matrix[x]))]
	
	return matrix
	
if __name__ == "__main__":
	input = file_to_matrix(sys.argv[1])
	print "Input Matrix:"
	print_matrix(input)
	print
	
	output = do_math(input)
	
	print "Output Matrix:"
	print_matrix(output)