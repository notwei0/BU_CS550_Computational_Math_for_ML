import numpy as np
import matplotlib.pyplot as plt

# defines matrices and sets theta
tpi4 = np.pi/4
tpi6 = np.pi/6

problem2 = [
    ("M1:",      np.array([[1.5, 0],             
                           [0, 1]])),

    ("M2:",      np.array([[1, 0],               
                           [0, 0.75]])),

    ("M3:",      np.array([[1, 2],               
                           [0, 1]])),

    ("M4:",      np.array([[1, 0],               
                           [1.25, 1]])),

    ("M5:",      np.array([[np.cos(tpi4), -np.sin(tpi4)], 
                           [np.sin(tpi4),  np.cos(tpi4)]])),

    ("M6:",      np.array([[np.cos(tpi6),  np.sin(tpi6)], 
                           [-np.sin(tpi6), np.cos(tpi6)]]))
]

# Print characteristic polynomial and eigenvalues
for name, M in problem2:
    tr  = np.trace(M)
    det = np.linalg.det(M)
    vals, vecs = np.linalg.eig(M)
    print(f"{name}")
    print(f"  P(eig) = eig^2 - {tr:.4f}λ + {det:.4f}")
    for i, (val, vec) in enumerate(zip(vals, vecs.T)):
        if np.isreal(val):
            print(f"  λ{i+1} = {val.real:.4f}, eigenvector = [{vec[0].real:.3f}, {vec[1].real:.3f}]")
        else:
            print(f"no real eigenvector")

# circle
theta  = np.linspace(0, 2*np.pi, 360)
circle = np.array([np.cos(theta), np.sin(theta)])

# plots the circles
# outside help from a python software developer
fig, axes = plt.subplots(2, 3, figsize=(13, 9))
for ax, (name, M) in zip(axes.flatten(), problem2):
    transformed = M @ circle
    ax.plot(circle[0], circle[1], "b--", label="Unit circle")
    ax.plot(transformed[0], transformed[1], "b-", label="Transformed")

    vals, vecs = np.linalg.eig(M)
    has_real = False
    for (val, vec), color in zip(zip(vals, vecs.T), ["red", "green"]):
        if np.isreal(val) and np.isreal(vec).all():
            v = vec.real * val.real
            ax.annotate("", xy=v, xytext=(0, 0),
                        arrowprops=dict(arrowstyle="->", color=color))
            ax.text(v[0], v[1], f"eigenvalue ={val.real:.2f}", color=color)
            has_real = True
    if not has_real:
        ax.text(-1, 0, "Complex eigenvalues")

    ax.set_title(name, fontsize=10)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.grid(True)

plt.suptitle("Problem 2")
plt.tight_layout()
plt.show()