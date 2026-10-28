import numpy as np

#tutor also helped me with this problem by hand and translating it into code
#b
print("eigenvalues:")
print("  eig = (5 +/- sqrt(5^2 + 4*2)) / 2")
print("      = (5 +/- sqrt(25 + 8)) / 2")
print("      = (5 +/- sqrt(33)) / 2")
print("  eig1 = (5 + sqrt(33)) / 2 = 5.3723")
print("  eig2 = (5 - sqrt(33)) / 2 = -0.3723")
 
#c
print("eigenvectors:")
print("  (A - eig*I)v = 0 using row 1: (1 - eig)*v1 + 2*v2 = 0")
print("  eig1: v1 = 2 / (5.3723 - 1) = 2 / 4.3723 = 0.4574, v2 = 1  ->  [0.4574, 1]")
print("  eig2: v1 = 2 / (-0.3723 - 1) = 2 / -1.3723 = -1.4574, v2 = 1  ->  [-1.4574, 1]")
 
#d
print("Cayley-Hamilton to verify P(A) = A^2 - 5A - 2I = 0:")
print("  A^2 = [[1*1+2*3, 1*2+2*4], [3*1+4*3, 3*2+4*4]] = [[7, 10], [15, 22]]")
print("  5A  = [[5, 10], [15, 20]]")
print("  2I  = [[2, 0], [0, 2]]")
print("  A^2 - 5A - 2I = [[7-5-2, 10-10-0], [15-15-0, 22-20-2]] = [[0, 0], [0, 0]]")


A = np.array([[1, 2],
              [3, 4]], dtype=float)
#characteristic of the polynomial P(eigen)
#outside help from a software dev to use trace
tr  = np.trace(A)
det = np.linalg.det(A)
print(f"P(eig) = eig^2 - {tr:.0f}eig + ({det:.0f})")

# eigenvalues
vals, vecs = np.linalg.eig(A)
print(f"eigenvalues:")
for i, v in enumerate(vals):
    print(f"eig{i+1} = {v:.4f}")
print()

# eigenvectors
print(f"eigenvectors:")
for i, (val, vec) in enumerate(zip(vals, vecs.T)):
    print(f"eig{i+1} = {val:.4f}  to  [{vec[0]:.4f}, {vec[1]:.4f}]")
print()

# d) Cayley-Hamilton: P(A) = A^2 - 5A - 2I should = zero matrix
PA = np.linalg.matrix_power(A, 2) - 5*A - 2*np.eye(2)
print(f"P(A) = A^2 - 5A - 2I =")
print(np.round(PA, 4))
print("zero matrix confirmed" if np.allclose(PA, 0) else "not zero matrix")
