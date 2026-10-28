import sympy as sp

# cross terms get split in half between the symmetric off-diagonal entries
A = sp.Matrix([
    [2,  10, -2],
    [10,  5,  8],
    [-2,  8, 11]
])

print("A =")
sp.pprint(A) #this prints the matrix in a nice format

eigenvals = A.eigenvals() 
print("eigenvalues:")
for val, eig in eigenvals.items():
    print(round(float(val), 1))

# positive-definite if all eigenvalues > 0
evals_numeric = [sp.N(v) for v in eigenvals.keys()]
pos_def = all(v > 0 for v in evals_numeric)
print("positive-definite:", pos_def)