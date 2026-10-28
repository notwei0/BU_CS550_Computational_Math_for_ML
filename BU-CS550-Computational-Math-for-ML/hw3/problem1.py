import numpy as np
import matplotlib.pyplot as plt

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

#creates an array for the original matrix
def original_matrix(transform):
    matrix = np.array([
        [1, 0],
        [0, 1]
    ])
    
    x = matrix[0]
    y = matrix[1]

    return transform(x, y)

def transform_square(transform, square):
    x = square[0]
    y = square[1]

    return transform(x, y)

#creates a function for each transformation
def m1(x,y):
    return np.array([
        x * 1.5,
        y
    ])

def m2(x,y):
    return np.array([
        x,
        y * 0.75
    ])

def m3(x,y):
    return np.array([
        x + 2 * y,
        y
    ])

def m4(x,y):
    return np.array([
        x,
        y + 1.25 * x
    ])

def m5(x,y):
    theta = np.pi / 4
    return np.array([
        x * np.cos(theta) - y * np.sin(theta),
        x * np.sin(theta) + y * np.cos(theta)
    ])

def m6(x,y):
    theta = -np.pi / 6
    return np.array([
        x * np.cos(theta) - y * np.sin(theta),
        x * np.sin(theta) + y * np.cos(theta)
    ])

#creates a list to call a for loop
problem1 = [
    ("M1", m1),
    ("M2", m2),
    ("M3", m3),
    ("M4", m4),
    ("M5", m5),
    ("M6", m6)
]

#prints the original square and the following transformations after
print(f"Original Square: \n{original_matrix(lambda x, y: np.array([x, y]))}")
for name, transform, in problem1:
    matrix = original_matrix(transform)
    print(f"{name}:")
    print(np.round(matrix, 3))
    print("New Vertices:")
    print_vertices(transform_square(transform, original_square))


#creates a plot for the original square and the following transformations after (used ax for the subplots)
fig, axes = plt.subplots(2, 3, figsize=(12, 8))
for name, transform, in problem1:
    transformed_square = transform_square(transform, original_square)
    ax = axes.flatten()[problem1.index((name, transform))]
    ax.plot(original_square[0], original_square[1], marker='o', label='Original Square')
    ax.plot(transformed_square[0], transformed_square[1], marker='o', label=f'{name} Transformed Square')
    ax.set_title(name)
    ax.set_xlim(-1, 4)
    ax.set_ylim(-1, 4)
    ax.legend()
plt.tight_layout()
plt.show()