import numpy as np
import matplotlib.pyplot as plt

# bisection method, first 3 iterations
# starting interval a = -3, b = 3
#only ai use is finding a good figsize

#equations
problem3 = [
    ("x^2 - 5",          lambda x: x**2 - 5, -3, 3),
    ("x^3 - 5",          lambda x: x**3 - 5, -3, 3),
    ("sqrt(x) - 1.5",    lambda x: np.sqrt(x) - 1.5, 0.01, 3),
    ("e^x - 2",          lambda x: np.exp(x) - 2, -3, 3),
    ("2^x - 0.5",        lambda x: 2**x - 0.5, -3, 3),
    ("log(x) - 1",       lambda x: np.log(x) - 1, 0.01, 3),
    ("sin(x) - 0.5",     lambda x: np.sin(x) - 0.5, -3, 3),
    ("cos(x) - 0.5",     lambda x: np.cos(x) - 0.5, -3, 3),
]

fig, axs = plt.subplots(4, 2, figsize=(11, 14)) 
axs = axs.flatten()
point_colors = ["red", "blue", "green"]
for ax, (title, f, lo, hi) in zip(axs, problem3):
    x = np.linspace(lo, hi, 1000)
    ax.plot(x, f(x), color="green")

    a, b = -3, 3
    #recieved help from a friend on this part on creating the if statements
    if lo > -3:
        a = lo
    for i in range(3):
        c = (a + b) / 2
        ax.scatter(c, f(c), color=point_colors[i])
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
    ax.set_title(title)
    ax.axhline(0, color="black")
    ax.set_xlim(lo, hi)
plt.tight_layout()
plt.show()