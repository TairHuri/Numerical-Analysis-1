"""
Tair Huri, 325329118
Noa Shem Tov, 207000134
AN HW1
"""
def PrintMatrix(matrix):
    """ Matrix Printing Function """
    for line in matrix:
        print('  '.join(map(str, line)))

def add_matrices(matrix1, matrix2):
    """ Matrix Add Matrices """
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def createMatrix(size):
    """ Matrix Creation Function """
    matrix = []
    print("Please enter the Mat\n")
    for i in range(size):
        row = []
        for j in range(size):
            row.append(int(input("Please enter the " + str(j+1) + " number in the " + str(i+1) + " row of the mat: ")))
        matrix.append(row)
    return matrix

def multiply_matrices(matrix1, matrix2):
    """ Matrix Multiply Matrices """
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(len(matrix2)):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        result.append(row)
    return result

size = int(input("Please enter the size of the mat "))
matrix1 = createMatrix(size)
matrix2 = createMatrix(size)
print("\nMatrix1 \n")
PrintMatrix(matrix1)
print("\nMatrix2 \n")
PrintMatrix(matrix2)
print("The Matrix Multiplication is", multiply_matrices(matrix1, matrix2))
print("The Matrix Addition is", add_matrices(matrix1, matrix2))
