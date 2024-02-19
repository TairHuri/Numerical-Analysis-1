# @source: https://github.com/lihiSabag/Numerical-Analysis-2023.git
# Date: 02 – 19 – 24
# Group:
# Yael Haim         	    324978261
# Tair Huri 	            325329118
# Noa Shem Tov              207000134
# Git: https://github.com/TairHuri/Numerical-Analysis-1
# Name:  Noa Shem Tov, 207000134

from colors import bcolors
from matrix_utility import row_addition_elementary_matrix, scalar_multiplication_elementary_matrix, print_matrix
import numpy as np


"""
Function that find the inverse of non-singular matrix
The function performs elementary row operations to transform it into the identity matrix. 
The resulting identity matrix will be the inverse of the input matrix if it is non-singular.
 If the input matrix is singular (i.e., its diagonal elements become zero during row operations), it raises an error.
"""

def inverse(matrix):
    print(bcolors.OKBLUE, f"=================== Finding the inverse of a non-singular matrix using elementary row operations ===================\n {matrix}\n", bcolors.ENDC)
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input matrix must be square.")

    n = matrix.shape[0]
    identity = np.identity(n)

    # Perform row operations to transform the input matrix into the identity matrix
    for i in range(n):
        if matrix[i, i] == 0:
            raise ValueError("Matrix is singular, cannot find its inverse.")

        if matrix[i, i] != 1:
            # Scale the current row to make the diagonal element 1
            scalar = 1.0 / matrix[i, i]
            elementary_matrix = scalar_multiplication_elementary_matrix(n, i, scalar)
            print(f"elementary matrix to make the diagonal element 1 :\n {elementary_matrix} \n")
            matrix = np.dot(elementary_matrix, matrix)
            print(f"The matrix after elementary operation :\n {matrix}")
            print(bcolors.OKGREEN, "------------------------------------------------------------------------------------------------------------------",  bcolors.ENDC)
            identity = np.dot(elementary_matrix, identity)

    # Zero out the elements above and below the diagonal
        for j in range(n):
            if i < j:
                scalar = -matrix[j, i]
                elementary_matrix = row_addition_elementary_matrix(n, j, i, scalar)
                print(f"elementary matrix for R{j+1} = R{j+1} + ({scalar}R{i+1}):\n {elementary_matrix} \n")
                matrix = np.dot(elementary_matrix, matrix)
                print(f"The matrix after elementary operation :\n {matrix}")
                print(bcolors.OKGREEN, "------------------------------------------------------------------------------------------------------------------",
                      bcolors.ENDC)
                identity = np.dot(elementary_matrix, identity)
    # Zero out the elements below the diagonal
    for i in range(n - 1, -1, -1):
        if matrix[i, i] == 0:
            raise ValueError("Matrix is singular, cannot find its inverse.")
        for j in range(n-1, -1, -1):
            if i > j:
                scalar = -matrix[j, i]
                elementary_matrix = row_addition_elementary_matrix(n, j, i, scalar)
                print(f"elementary matrix for R{j + 1} = R{j + 1} + ({scalar}R{i + 1}):\n {elementary_matrix} \n")
                matrix = np.dot(elementary_matrix, matrix)
                print(f"The matrix after elementary operation :\n {matrix}")
                print(bcolors.OKGREEN,
                      "------------------------------------------------------------------------------------------------------------------",
                        bcolors.ENDC)
                identity = np.dot(elementary_matrix, identity)
    return identity

if __name__ == '__main__':

    print(
        " @source: https://github.com/lihiSabag/Numerical-Analysis-2023.git\n Date: 02 – 19 – 24 \n Group: \n Yael Haim           324978261"
        "\n Tair Huri           325329118\n Noa Shem Tov        207000134\n Git: https://github.com/TairHuri/Numerical-Analysis-1"
        "\n Name:  Noa Shem Tov  207000134")

    A = np.array([[2, 3, 1],
                  [3, 4, 2],
                  [4, 1, 5]])

    try:
        A_inverse = inverse(A)
        print(bcolors.OKBLUE, "\nInverse of matrix A: \n", A_inverse)
        print("=====================================================================================================================", bcolors.ENDC)

    except ValueError as e:
        print(str(e))

