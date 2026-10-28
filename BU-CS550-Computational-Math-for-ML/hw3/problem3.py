import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

#creates a matrix for the original square
original_square = np.array([
    [0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0]
])

def print_vertices(square):
    vertex_names = ["A'", "B'", "C'", "D'"]

    for i, vertex in enumerate(vertex_names):
        x_value = square[0, i]
        y_value = square[1, i]
        print(f"{vertex} = ({x_value:.3f}, {y_value:.3f})")

#creates a function for each transformation
m1 = np.array([
    [1.5, 0],
    [0, 1]
])

m2 = np.array([
    [1, 0],
    [0, 0.75]
])

m3 = np.array([
    [1, 2],
    [0, 1]
])
m4 = np.array([
    [1, 0],
    [1.25, 1]
])

theta = np.pi / 4
m5 = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta), np.cos(theta)]
])

theta = -np.pi / 6
m6 = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta), np.cos(theta)]
])

#does the math to create a new polygon A'B'C'D' using the combination of the transformations and prints the vertices of the new polygon
T1 = np.linalg.matrix_power(m1, 2) @ np.linalg.matrix_power(m3, 3) @ m5
T2 = np.linalg.inv(m2) @ np.linalg.matrix_power(np.linalg.inv(m4), 2) @ m6

#applies transformations to original square
transform0 = T1 @ original_square
transform1 = T2 @ original_square

#print the new unique vertices
print("Transformation 1:")
print_vertices(transform0)

print("Transformation 2:")
print_vertices(transform1)

#prints the unique polygon vertices for each transformation
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(transform0[0], transform0[1], marker='o')
plt.title("Transformation 1")
plt.subplot(1, 2, 2)
plt.plot(transform1[0], transform1[1], marker='o')
plt.title("Transformation 2")
plt.show()
