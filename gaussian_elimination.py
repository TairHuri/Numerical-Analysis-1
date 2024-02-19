# @source: https://github.com/lihiSabag/Numerical-Analysis-2023.git
# Date: 02 – 19 – 24
# Group:
# Yael Haim         	    324978261
# Tair Huri 	            325329118
# Noa Shem Tov              207000134
# Git: https://github.com/TairHuri/Numerical-Analysis-1
# Name:  Noa Shem Tov, 207000134


import numpy as np
from colors import bcolors
from Matrix.inverse_matrix import inverse
from matrix_utility import swap_row

def gaussianElimination(mat):
    N = len(mat)
    singular_flag = forward_substitution(mat)
    if singular_flag != -1:

        if mat[singular_flag][N]:
            return "Singular Matrix (Inconsistent System)"
        else:
            return "Singular Matrix (May have infinitely many solutions)"

    # if matrix is non-singular: get solution to system using backward substitution
    return backward_substitution(mat)

def forward_substitution(mat):
    N = len(mat)
    for k in range(N):

        # Partial Pivoting: Find the pivot row with the largest absolute value in the current column
        pivot_row = k
        v_max = mat[pivot_row][k]
        for i in range(k + 1, N):
            if abs(mat[i][k]) > v_max:
                v_max = mat[i][k]
                pivot_row = i

        # if a principal diagonal element is zero,it denotes that matrix is singular,
        # and will lead to a division-by-zero later.
        if not mat[k][pivot_row]:
            return k  # Matrix is singular

        # Swap the current row with the pivot row
        if pivot_row != k:
            swap_row(mat, k, pivot_row)
        # End Partial Pivoting

        for i in range(k + 1, N):

            #  Compute the multiplier
            m = (mat[i][k] / mat[k][k])

            # subtract fth multiple of corresponding kth row element
            for j in range(k + 1, N + 1):
                mat[i][j] -= (mat[k][j] * m)
                if abs(mat[i][j]) < np.finfo(float).eps:
                    mat[i][j] = 0

            # filling lower triangular matrix with zeros
            mat[i][k] = 0

    return -1
# function to calculate the values of the unknowns
def backward_substitution(mat):
    N = len(mat)
    x = np.zeros(N)  # An array to store solution

    # Start calculating from last equation up to the first
    for i in range(N - 1, -1, -1):

        x[i] = mat[i][N]

        # Initialize j to i+1 since matrix is upper triangular
        for j in range(i + 1, N):
            x[i] -= mat[i][j] * x[j]

        x[i] = (x[i] / mat[i][i])

    return x
def norm(mat):
    size = len(mat)
    max_row = 0
    for row in range(size):
        sum_row = 0
        for col in range(size):
            sum_row += abs(mat[row][col])
        if sum_row > max_row:
            max_row = sum_row
    return max_row

if __name__ == '__main__':

    print(" @source: https://github.com/lihiSabag/Numerical-Analysis-2023.git\n Date: 02 – 19 – 24 \n Group: \n Yael Haim           324978261"
          "\n Tair Huri           325329118\n Noa Shem Tov        207000134\n Git: https://github.com/TairHuri/Numerical-Analysis-1"
          "\n Name:  Noa Shem Tov  207000134")

    A_b = [
        [1,  -1,   2,  -1,  -8],
        [2,  -2,   3,  -3, -20],
        [1,   1,   1,   0,  -2],
        [1,  -1,   4,   3,   4]]
    AB = [
         [1,   2,     3,    4,     5],
         [2,   3,     4,    5,     1],
         [8,   8,     8,    8,     1],
         [24, 15,     22,   1,     8],]
    CB = [[2, 3, 1, 2],
          [3, 4, 2, 6],
          [4, 1, 5, 0]]

    result = gaussianElimination(A_b)
    if isinstance(result, str):
        print(result)
    else:
        print(bcolors.OKBLUE,"\nSolution for the system:")
        for x in result:
            print("{:.6f}".format(x))
    print("\n")
    result = gaussianElimination(AB)
    if isinstance(result, str):
        print(result)
    else:
        print(bcolors.OKBLUE,"\nSolution for the system:")
        for x in result:
            print("{:.6f}".format(x))
    result = gaussianElimination(CB)
    if isinstance(result, str):
        print(result)
    else:
        print(bcolors.OKBLUE, "\nSolution for the system:")
        for x in result:
            print("{:.6f}".format(x))
    """norm_A = norm(A)
       norm_A_inv = norm(A_inverse)
       condA = norm_A * norm_A_inv
       if condA > 99:
           print("Cannot solve, change the conditions")
       print(bcolors.OKBLUE, "A:", bcolors.ENDC)
       print_matrix(A)
       print(bcolors.OKBLUE, "Max Norm of A:", bcolors.ENDC, norm_A, "\n")
       print(bcolors.OKBLUE, "max norm of the inverse of A:", bcolors.ENDC, norm_A_inv)"""