import numpy as np

#sets arrays for the matrixes
A = np.array([
    [1,2],
    [3,4]
], dtype = float)

B = np.array([
    [5,9],
    [2,5]
], dtype = float)

Aprime = np.linalg.inv(A)
Bprime = np.linalg.inv(B)

#preps for loop
problem5 = [
    ("A", A),
    ("B", B),
    ("B inverse", Bprime),
    ("A inverse", Aprime)
]

#math used to create the logarithms of the matrices
for name, matrix in problem5:
    I = np.eye(matrix.shape[0])
    x = matrix - I
    x_squared = x @ x
    x_cubed = x @ x @ x

    log_matrix = x - (x_squared / 2) + (x_cubed / 3)

    print(f"Log{name} using first 3 terms:")
    print(np.round(log_matrix, 3))