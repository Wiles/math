import sys

def file_to_matrix(file):
	list = []
	for line in open(file).readlines():
		list.append([(float(x)) for x in line.split()])
		
	return list

def print_results(matrix):
	for x in range(len(matrix)):
		print (matrix[x][len(matrix[x]) - 1])

def do_math(matrix):
	for x in range(len(matrix)):
		matrix[x] = [(z / matrix[x][x]) for z in matrix[x]]
		for y in range(len(matrix)):
			if x == y:
				continue
			matrix[y] = [(matrix[y][z] - matrix[x][z] * matrix[y][x]) for z in range(len(matrix[x]))]
	
	return matrix
	
if __name__ == "__main__":
	print_results(do_math(file_to_matrix(sys.argv[1])))