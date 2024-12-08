def load_matrix(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    matrix = [list(map(int, line.split())) for line in lines]

    if all(len(row) == len(matrix[0]) for row in matrix):
        return matrix
    else:
        return False
result=load_matrix('matriza.txt')
print(result)