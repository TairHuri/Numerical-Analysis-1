import numpy as np
def gaussianElimination(mat):
    N = len(mat)
    singular_flag = forward_substitution(mat)
    if singular_flag != -1:

        if mat[singular_flag][N]:
            return "Singular Matrix (Inconsistent System)"
        else:
            return "Singular Matrix (May have infinitely many solutions)"

# if matrix is non-singular:
    forward_substitution_to_diagonal(mat)
    # get solution to system using backward substitution
    return backward_substitution(mat)


# The function receives an upper triangular matrix and returns a fully ranked matrix
def forward_substitution(mat):
    N = len(mat)
    for k in range(N):
        pivot_row = k
        v_max = abs(mat[k][k])  # Setting the maximum value to the diagonal element itself
        for i in range(k + 1, N):
            if abs(mat[i][k]) > v_max:
                v_max = abs(mat[i][k])
                pivot_row = i

        if not mat[pivot_row][k]:  # Checking if the diagonal element is zero
            return k  # Matrix is singular

        # Swap the current row with the pivot row
        if pivot_row != k:
            # Swap entire rows, including the augmented column
            SaveRowi = mat[k].copy()
            mat[k] = mat[pivot_row]
            mat[pivot_row] = SaveRowi
        # End Partial Pivoting
        for i in range(k + 1, N):
            m = (mat[i][k] / mat[k][k])
            for j in range(k + 1, N + 1):
                mat[i][j] -= (mat[k][j] * m)
                if abs(mat[i][j]) < 1e-10:  # Small values are treated as zeros
                    mat[i][j] = 0

            mat[i][k] = 0  # Ensure lower triangular elements are zeroed out
    return -1

# function to calculate the values of the unknowns
def forward_substitution_to_diagonal(mat):
    N = len(mat)
    for k in range(N - 1, -1, -1):
        scalar = mat[k][k]
        for j in range(N + 1):
            mat[k][j] /= scalar

        for i in range(k - 1, -1, -1):
            scalar = mat[i][k]
            for j in range(N + 1):
                mat[i][j] -= mat[k][j] * scalar

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
def polynomialInterpolation(table_points, x):
    print("\033[94m" + "Polynomial Interpolation" + "\033[0m")
    matrix = Prerequisite(table_points)
    if matrix is None:
        return
    b = [[point[1]] for point in table_points]
    matrixNew = np.hstack((matrix, b))
    print("The matrix obtained from the points: "'\n', np.array(matrix))
    print("\nb vector: "'\n',np.array(b))
    matrixSol = gaussianElimination(matrixNew)
    if matrixSol is not None:
        print("\nResult Gauss: ",'\n', np.array(matrixSol))
        result = sum([matrixSol[i] * (x ** i) for i in range(len(matrixSol))])
        print("\nThe polynom:")
        print('P(X) = '+'+'.join([ '('+str(matrixSol[i])+') * x^' + str(i) + ' ' for i in range(len(matrixSol))]))
        print(f"\nThe Result of P(X={x}) is:")
        print(result)
        return result
    return None

def Prerequisite(table_points):
    matrix = [[point[0] ** i for i in range(len(table_points))] for point in table_points]  # Makes the initial matrix
    if not np.linalg.det(matrix):
        print("Singular Matrix")
        return None
    return matrix
def linearInterpolation(table_points, point):
    print("\033[94m" + "linear Interpolation" + "\033[0m")
    print("Table Points: ",table_points)
    print("Finding an approximation to the point: ", x)
    length = len(table_points)
    for i in range(length - 1):
        if table_points[i][0] <= point <= table_points[i + 1][0]:
            x1 = table_points[i][0]
            x2 = table_points[i + 1][0]
            y1 = table_points[i][1]
            y2 = table_points[i + 1][1]
            result = (((y1 - y2) / (x1 - x2)) * point) + ((y2 * x1) - (y1 * x2)) / (x1 - x2)
            print( "\nThe approximation (interpolation) of the point ", point, " is: ",round(result, 4))
            return
    x1 = table_points[- 2][0]
    x2 = table_points[- 1][0]
    y1 = table_points[- 2][1]
    y2 = table_points[- 1][1]
    m = (y1 - y2) / (x1 - x2)
    b = y1 - m * x1
    result = m * point + b
    print("\nThe approximation (extrapolation) of the point ", point, " is: ",round(result, 4))


def lagrange_interpolation(table_points, x):
    print("\033[94m" + "Lagrange Interpolation" + "\033[0m")
    n = 3
    result = 0.0
    for i in range(n):
        term = table_points[i][1]
        for j in range(n):
            if i != j:
                term *= (x - table_points[j][0]) / (table_points[i][0] - table_points[j][0])
        result += term
    return result

def GetTableValueLinear():
    n = int(input("Enter the number of points: "))
    table_points = []
    for i in range(n):
        point_input = input(f"Enter point {i + 1} separated by comma (x, y): ")
        point = point_input.strip().replace('(', '').replace(')', '').split(",")
        try:
            table_points.append((float(point[0]), float(point[1])))
        except ValueError:
            print("Invalid input. Please enter points in the format x, y with numeric values.")
            return []
    return table_points

def GetTableValueLagrangeOrPolynomial():
    n = 3
    table_points = []
    for i in range(n):
        point_input = input(f"Enter point {i + 1} separated by comma (x, y): ")
        point = point_input.strip().replace('(', '').replace(')', '').split(",")
        try:
            table_points.append((float(point[0]), float(point[1])))
        except ValueError:
            print("Invalid input. Please enter points in the format x, y with numeric values.")
            return []
    return table_points


if __name__ == '__main__':
    print("----------------- Interpolation & Extrapolation Methods -----------------\n")
    Choice = input("Enter 1 for Polynomial, 2 for linear, 3 for lagrange\n")
    while Choice not in ['1', '2', '3']:
        Choice = input("Enter 1 for Polynomial, 2 for linear, 3 for lagrange\n")
    if Choice == '1':
        table_points = GetTableValueLagrangeOrPolynomial()
        if table_points != []:
            x = float(input("Enter x = "))
            polynomialInterpolation(table_points, x)
    elif Choice == '2':
        table_points = GetTableValueLinear()
        if table_points != []:
            x = float(input("Enter x = "))
            linearInterpolation(table_points, x)
    else:
        table_points = GetTableValueLagrangeOrPolynomial()
        if table_points != []:
            x = float(input("Enter x = "))
            y_interpolate = lagrange_interpolation(table_points, x)
            print("\nInterpolated value at" + "\033[94m" + f" x = {x}" + "\033[0m" + " is " + "\033[94m" + f"y = {round(y_interpolate, 4)}")

