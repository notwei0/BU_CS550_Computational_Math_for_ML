import numpy as np
import matplotlib.pyplot as plt

#sets the rule to create the circle and angle theta
theta = np.linspace(0, 2*np.pi)
circle = np.array([np.cos(theta), np.sin(theta)])

#declares values for M5 rotation
cospi4 = np.cos(np.pi/4)
sinpi4 = np.sin(np.pi/4)

#declares values for M6 rotation 
cospi6 = np.cos(np.pi/6)
sinpi6 = np.sin(np.pi/6)

#tuple for all the matrices
transformations = {
    "M1":        np.array([[1.5, 0],
                           [0, 1]]),

    "M2":        np.array([[1, 0],
                           [0, 0.75]]),

    "M3":        np.array([[1, 2],    
                           [0, 1]]),

    "M4":        np.array([[1, 0],    
                           [1.25, 1]]),

    "M5":        np.array([[cospi4, -sinpi4], 
                           [sinpi4, cospi4]]),

    "M6":        np.array([[cospi6, sinpi6],  
                           [-sinpi6, cospi6]]),
}

#plots points 
fig, axes = plt.subplots(2, 3, figsize=(12, 8))
#this is new notation found and tweaked via https://stackoverflow.com/questions/6963035/how-to-set-common-axes-labels-for-subplots
for ax, (name, M) in zip(axes.flatten(), transformations):
    transformed = M @ circle
    ax.plot(circle[0], circle[1], "b-", label="Original")
    ax.plot(transformed[0], transformed[1], "r-", label="Transformed")
    area = abs(np.linalg.det(M)) * np.pi
    ax.set_title(f"{name}\narea = {area:.4f}")
    ax.set_aspect("equal"); ax.legend(fontsize=7); ax.grid(True)
plt.tight_layout()
plt.show()
#claude ai for line 40

#You want to iterate over both your `transformations` dict and the `axes` grid simultaneously. The trick is that `axes` is a 2D array shape `(2,3)`, so you'll want to flatten it first to make looping easier.

#Think about what `axes.flatten()` gives you, and then how `zip()` lets you pair two iterables together:

#```python
#for ax, (name, M) in zip(axes.flatten(), transformations.items()):
    # ax is the current subplot
    # name is the string key like "M1"
    # M is the matrix

#From there, inside the loop you need to:
#1. Apply `M` to `circle` — think about how matrix multiplication works with `@` or `np.dot`
#2. Plot the original circle on `ax`
#3. Plot the transformed result on `ax`
#4. Set a title using `name`

#What does `M @ circle` give you, and how would you unpack the x and y coordinates from it?