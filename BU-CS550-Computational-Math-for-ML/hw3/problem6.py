import numpy as np
from numpy import array, zeros

#creates a tuple for the systems for a single for loop to go through all calculations and prints
systems = [
    ("6.1", [[2, 3],  
             [2, -1]],              [8, 0]),

    ("6.2", [[1, 2],  
             [2, 1]],               [-2, 2]),
    ("6.3", [[2, 3, 4], 
             [1, -1, 1], 
             [2, -1, 1]],           [4, 1, 1]),
    ("6.4", [[1, 1, 1], 
             [2, 1, 1], 
             [1, 2, 2]],            [1, 2, 1]),
]

#elimination
for name, raw_A, raw_b in systems:
    A = np.array(raw_A, dtype=float)
    b = np.array(raw_b, dtype=float)
    n = len(b)
    singular = False

    #checking for singularity and doing forward elimination
    for k in range(n):
        if abs(A[k, k]) < 1e-9:
            print(f"System {name} has no unique solution")
            singular = True
            break
        for i in range(k + 1, n):
            if A[i, k] == 0:
                continue
            factor = A[i, k] / A[k, k]
            for j in range(k, n):
                A[i, j] = A[i, j] - factor * A[k, j]
            b[i] = b[i] - factor * b[k]
    #does backward elimination
    if not singular:
        x = np.zeros(n, dtype=float)
        x[n-1] = b[n-1] / A[n-1, n-1]
        for i in range(n-2, -1, -1):
            sum_of = 0
            for j in range(i+1, n):
                sum_of += A[i, j] * x[j]
            x[i] = (b[i] - sum_of) / A[i, i]
        #prints solution
        print(f"Solution to System {name}:")
        for k, val in enumerate(x):
            print(f"  {['x','y','z'][k]} = {round(val, 3)}")

#used a youtube video to learn the math notation for doing guass elimination and self taught through trial and error on how to integrate it into an array
#https://www.youtube.com/watch?v=ZDxONtacA_4