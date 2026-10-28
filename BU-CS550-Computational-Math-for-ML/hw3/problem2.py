import numpy as np

def original_matrix(transform):
    matrix = np.array([
        [1, 0],
        [0, 1]
    ])
    
    x = matrix[0]
    y = matrix[1]
    return transform(x, y)


#creates a matrix for the original square
original_square = np.array([
    [0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0]
])

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
problem2 = [
    ("M1", m1),
    ("M2", m2),
    ("M3", m3),
    ("M4", m4),
    ("M5", m5),
    ("M6", m6)
]

#test prints the matrixes for the transformations
print(f"Original Square: \n{original_matrix(lambda x, y: np.array([x, y]))}")
for name, transform, in problem2:
    matrix = original_matrix(transform)
    print(f"{name}:")
    print(np.round(matrix, 3))

#solves the matrix for the inverse of the transformations
print("\nInverse Transformations:")
for name, transform, in problem2:
    matrix = original_matrix(transform)
    inverse = np.linalg.inv(matrix)
    print(f"{name} Inverse:")
    print(np.round(inverse, 3))