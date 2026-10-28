import numpy as np
from numpy import array, zeros

#creates an array for the matrixes
problem4 = [
    ("A", np.array([[1, 2],
                    [3, 4]])),

    ("B", np.array([[5, 9],
                    [2, 5]])),

    ("C", np.array([[2, 1, 0],
                    [3, 6, 1],
                    [5, 7, 1]]))
]

for name, matrix in problem4:
    #calls important variables
    matrix = np.array(matrix, dtype=float)
    n = matrix.shape[0]
    a = matrix.copy()
    inv = np.eye(n)
    singular = False

    #solves via forward elimination and checks for singularity 
    for k in range(n):
        if abs(a[k, k]) < 1e-9:
            print(f"Matrix {name} is singular, no inverse exists")
            singular = True
            break
        for i in range(k + 1, n):
            if a[i, k] == 0:
                continue
            factor = a[i, k] / a[k, k]
            for j in range(n):
                a[i, j] = a[i, j] - factor * a[k, j]
                inv[i, j] = inv[i, j] - factor * inv[k, j]

    if not singular:
        #solves back substitution
        for i in range(n - 1, -1, -1):
            pivot = a[i, i]
            a[i, :] = a[i, :] / pivot
            inv[i, :] = inv[i, :] / pivot
            for j in range(i - 1, -1, -1):
                factor = a[j, i]
                a[j, :] = a[j, :] - factor * a[i, :]
                inv[j, :] = inv[j, :] - factor * inv[i, :]
        print(f"Inverse of {name}:")
        print(np.round(inv, 3))

#used a youtube video to learn the math notation for doing guass elimination and self taught through trial and error on how to integrate it into an array
#https://www.youtube.com/watch?v=ZDxONtacA_4