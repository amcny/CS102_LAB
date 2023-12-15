def matrix_addition(mat1, mat2):
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]

def matrix_multiplication(mat1, mat2):
    return [[sum(mat1[i][k] * mat2[k][j] for k in range(len(mat2))) for j in range(len(mat2[0]))] for i in range(len(mat1))]
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Perform matrix addition
result_addition = matrix_addition(matrix1, matrix2)
print("Matrix Addition Result:")
for row in result_addition:
    print(row)

# Perform matrix multiplication
result_multiplication = matrix_multiplication(matrix1, matrix2)
print("\nMatrix Multiplication Result:")
for row in result_multiplication:
    print(row)