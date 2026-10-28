import numpy as np
import matplotlib.pyplot as plt

#defines matrices
#not typing pi anymore, too much work
t4 = np.pi/4
t6 = np.pi/6

M1 = np.array([[1.5, 0],                  
               [0, 1]])

M2 = np.array([[1, 0],                    
               [0, 0.75]])

M3 = np.array([[1, 2],                    
               [0, 1]])

M4 = np.array([[1, 0],                    
               [1.25, 1]])

M5 = np.array([[np.cos(t4), -np.sin(t4)], 
               [np.sin(t4),  np.cos(t4)]])

M6 = np.array([[np.cos(t6),  np.sin(t6)], 
               [-np.sin(t6), np.cos(t6)]])

# Composite transformations
# a) M1² @ M3³ @ M5
A = np.linalg.matrix_power(M1, 2) @ np.linalg.matrix_power(M3, 3) @ M5

# b) M2⁻¹ @ M4⁻² @ M6
B = np.linalg.matrix_power(M2, -1) @ np.linalg.matrix_power(M4, -2) @ M6

# Print matrices and areas
for label, combo in [
    ("(M1^2)(M3^3)M5",       A),
    ("(M2^-1)(M4^-2)M6",       B),
]:
    
    det  = np.linalg.det(combo)
    area = abs(det) * np.pi
    print(f"{label}")
    print(f"  Combined matrix:")
    print(f"{np.round(combo, 4)}")
    print(f"  det = {det:.4f}")
    print(f"  Area = {area:.4f}\n")

# Unit circle
theta  = np.linspace(0, 2*np.pi, 500)
circle = np.array([np.cos(theta), np.sin(theta)])

# plots the circles and transformations
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
for ax, (label, combo) in zip(axes, [("(M1^2)(M3^3)M5", A), ("(M2^-1)(M4^-2)M6", B)]):
    transformed = combo @ circle
    area = abs(np.linalg.det(combo)) * np.pi
    ax.plot(circle[0], circle[1], 'b--',label='Unit circle')
    ax.plot(transformed[0], transformed[1], 'r-', label='Transformed')
    ax.set_title(f"{label}\nArea ≈ {area:.4f}")
    ax.set_aspect('equal')
    ax.axhline(0, color='k')
    ax.axvline(0, color='k')
    ax.legend()
    ax.grid(True)

plt.suptitle("Problem 3")
plt.tight_layout()
plt.show()