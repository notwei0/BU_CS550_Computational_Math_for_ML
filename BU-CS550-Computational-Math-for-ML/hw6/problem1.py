import numpy as np
import matplotlib.pyplot as plt

h = 0.00001

#equal to f'(a) using the definition of the derivative
def df(f, a):
    return (f(a+h) - f(a)) / h

def n(f, a):
    return a - f(a)/df(f, a)

#equations
problem1 = [
    ("x^2 - 5",           lambda x: x**2 - 5, -3, 3),
    ("x^3 - 5",           lambda x: x**3 - 5, -3, 3),
    ("sqrt(x) - 1.5",     lambda x: np.sqrt(x) - 1.5, 0.01, 3),
    ("e^x - 2",           lambda x: np.exp(x) - 2, -3, 3),
    ("2^x - 0.5",         lambda x: 2**x - 0.5, -3, 3),
    ("log(x) - 1",        lambda x: np.log(x) - 1, 0.01, 3),
    ("sin(x) - 0.5",      lambda x: np.sin(x) - 0.5, -3, 3),
    ("cos(x) - 0.5",      lambda x: np.cos(x) - 0.5, -3, 3),
]

fig, axs = plt.subplots(4, 2, figsize=(11, 14))
axs = axs.flatten()
tangent_colors = ["red", "blue", "green"]
for ax, (title, f, lo, hi) in zip(axs, problem1):
    x = np.linspace(lo, hi, 1000)
    ax.plot(x, f(x), color="green")
    a = 3.0
    for i in range(3):
        tan_line = df(f, a)*(x - a) + f(a)
        ax.plot(x, tan_line, color=tangent_colors[i])
        a = n(f, a)
    ax.set_title(title)
    ax.axhline(0, color="black")
    ax.set_xlim(lo, hi)
plt.tight_layout()
plt.show()