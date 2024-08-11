from numpy import matrix


# Function to print the matrix
def printMat(a, r, c):

    for i in range(r):
        for j in range(c):
            print(a[i][j], end=" ")
        print()
    print()


# Function to print the matrix
def printt(display, matrix, start_row, start_column, end_row, end_column):
    print(display + " =>\n")
    for i in range(start_row, end_row + 1):
        for j in range(start_column, end_column + 1):
            print(matrix[i][j], end=" ")
        print()
    print()


# Function to add two matrices
def add_matrix(matrix_A, matrix_B, matrix_C, split_index):
    for i in range(split_index):
        for j in range(split_index):
            matrix_C[i][j] = matrix_A[i][j] + matrix_B[i][j]


# Function to initialize matrix with zeros
def initWithZeros(a, r, c):
    for i in range(r):
        for j in range(c):
            a[i][j] = 0


# Function to multiply two matrices


import numpy as np


def split(matrix):
    """
    Splits a given matrix into quarters.
    Input: nxn matrix
    Output: tuple containing 4 n/2 x n/2 matrices corresponding to a, b, c, d
    """
    row, col = matrix.shape
    row2, col2 = row // 2, col // 2
    return (
        matrix[:row2, :col2],
        matrix[:row2, col2:],
        matrix[row2:, :col2],
        matrix[row2:, col2:],
    )


def strassen(x, y):
    """
    Computes matrix product by divide and conquer approach, recursively.
    Input: nxn matrices x and y
    Output: nxn matrix, product of x and y
    """

    # Base case when size of matrices is 1x1
    if len(x) == 1:
        return x * y

    # Splitting the matrices into quadrants. This will be done recursively
    # until the base case is reached.
    a, b, c, d = split(x)
    e, f, g, h = split(y)

    # Computing the 7 products, recursively (p1, p2...p7)
    p1 = strassen(a, f - h)
    p2 = strassen(a + b, h)
    p3 = strassen(c + d, e)
    p4 = strassen(d, g - e)
    p5 = strassen(a + d, e + h)
    p6 = strassen(b - d, g + h)
    p7 = strassen(a - c, e + f)
    print(
        f"7 Values",
        [f"index: {index} {x}" for index, x in enumerate([p1, p2, p3, p4, p5, p6, p7])],
    )
    # Computing the values of the 4 quadrants of the final matrix c
    c00: matrix = p5 + p4 - p2 + p6
    c01: matrix = p1 + p2
    c10: matrix = p3 + p4
    c11: matrix = p1 + p5 - p3 - p7
    print(c00, c01, c10, c11)

    # Combining the 4 quadrants into a single matrix by stacking horizontally and vertically.
    c = np.vstack((np.hstack([c00, c01]), np.hstack([c10, c11])))
    return c


# Driver Code
matrix_A = np.matrix(
    data=[
        [4, 2],
        [6, 7],
    ]
)
# matrix_A = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [2, 2, 2, 2]]

print("Array A =>")
# printMat(matrix_A, 2, 2)
print(matrix_A)

matrix_B: matrix = np.matrix(
    data=[
        [1, 5],
        [3, 8],
    ]
)


# matrix_B = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [2, 2, 2, 2]]

print("Array B =>")
# printMat(matrix_B, 2, 2)
print(matrix_B)

result_matrix = strassen(matrix_A, matrix_B)

print("Result Array =>")
# printMat(result_matrix, 2, 2)
print(result_matrix)
