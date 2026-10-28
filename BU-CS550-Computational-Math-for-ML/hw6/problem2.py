import numpy as np
import matplotlib.pyplot as plt

#equations for secant method
def secant_line(f, a, b, x):
    slope = (f(b) - f(a)) / (b - a)
    return slope*(x - a) + f(a)

def secant_step(f, a, b):
    return b - f(b)*(b - a)/(f(b) - f(a))

#equations
problem2 = [
    ("x^2 - 5",            lambda x: x**2 - 5, -3, 3),
    ("x^3 - 5",            lambda x: x**3 - 5, -3, 3),
    ("sqrt(x) - 1.5",      lambda x: np.sqrt(x) - 1.5, 0.01, 3),
    ("e^x - 2",            lambda x: np.exp(x) - 2, -3, 3),
    ("2^x - 0.5",          lambda x: 2**x - 0.5, -3, 3),
    ("log(x) - 1",         lambda x: np.log(x) - 1, 0.01, 3),
    ("sin(x) - 0.5",       lambda x: np.sin(x) - 0.5, -3, 3),
    ("cos(x) - 0.5",       lambda x: np.cos(x) - 0.5, -3, 3),
]

#plots the secant lines
fig, axs = plt.subplots(4, 2, figsize=(11, 14))
axs = axs.flatten()
secant_colors = ["red", "blue", "green"]
for ax, (title, f, lo, hi) in zip(axs, problem2):
    x = np.linspace(lo, hi, 1000)
    ax.plot(x, f(x), color="green")
    x_prev, x_curr = 3.0, 2.0
    for i in range(3):
        sec_line = secant_line(f, x_prev, x_curr, x)
        ax.plot(x, sec_line, color=secant_colors[i])
        x_next = secant_step(f, x_prev, x_curr)
        x_prev, x_curr = x_curr, x_next
    ax.set_title(title)
    ax.axhline(0, color="black")
    ax.set_xlim(lo, hi)
plt.tight_layout()
plt.show()