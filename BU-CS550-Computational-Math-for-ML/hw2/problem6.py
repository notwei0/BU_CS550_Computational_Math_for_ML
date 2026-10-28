import numpy as np
import scipy.integrate as spi

#symbols and values n = 3 and a and b as 1 and 5 respectively, excludes x with the use of lambda functions for the functions
n = 3
a, b = 1, 5

problem6 = [
    ("1", lambda x: 2 + 0*x),
    ("2", lambda x: x + 1),
    ("3", lambda x: 2*x**2 + x),
    ("4", lambda x: x**n + n),
    ("5", lambda x: 2*np.sqrt(x)),
    ("6", lambda x: np.exp(x + 1)),
    ("7", lambda x: 3**x),
    ("8", lambda x: np.log(x) + 1),
    ("9", lambda x: np.sin(x + np.pi/6)),
    ("10", lambda x: np.cos(x + np.pi/6)),   
]

#solves the integrals for the functions using fixed quadrature method with limits from 1 to 5
print("Fixed Quadrature Method\n")

for label, f in problem6:
    res, _ = spi.fixed_quad(f, a, b)
    print(f"#{label}  Result is {res:.4f}")

#solves the integrals for the functions using the trapezoid method with limits from 1 to 5
print("\nTrapezoid Method\n")

for label, f in problem6:
    step = 1e-4
    x = np.arange(a, b, step)
    y = f(x)
    res = spi.trapezoid(y, x)
    print(f"#{label}  Result is {res:.4f}")

#solves the integrals for the functions using the Simpson's method with limits from 1 to 5
print("\nSimpson's Method\n")

for label, f in problem6:
    step = 1e-4
    x = np.arange(a, b, step)
    y = f(x)
    res = spi.simpson(y, x)
    print(f"#{label}  Result is {res:.4f}")