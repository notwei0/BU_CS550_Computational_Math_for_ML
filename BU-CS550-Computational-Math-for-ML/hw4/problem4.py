import numpy as np

problem4 = [
("A",    np.array([[1, 4],
                   [2, 3]])),

("B",    np.array([[5,  19],
                  [-2,  5]])),

("C",    np.array([[2, 1, 9],
                   [5, 7, 1],
                   [4, 7, 1]]))
]

for name, matrices in problem4:
    det  = np.linalg.det(matrices)
    L1   = np.linalg.norm(matrices)
    print(f"matrix {name}:")
    print(f"det  = {det:.4f}")
    print(f"L1   = {L1:.4f}")
