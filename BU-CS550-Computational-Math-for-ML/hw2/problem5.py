import sympy as sym

#symbols and values
x = sym.symbols('x')
n = 3

#10 functions from Problem 4 (only f is written down)
problem5 = [
    ("1",  sym.Integer(2)),
    ("2",  x + 1),
    ("3",  2*x**2 + x),
    ("4",  x**n + n),
    ("5",  2*sym.sqrt(x)),
    ("6",  sym.exp(x + 1)),
    ("7",  sym.Integer(3)**x),
    ("8",  sym.log(x) + 1),
    ("9",  sym.sin(x + sym.pi/6)),
    ("10", sym.cos(x + sym.pi/6)),
]

#creates the equation for integrals for the equations with limits from 1 to 5
for label, f in problem5:
    integral = sym.integrate(f, (x, 1, 5))
    print(f"#{label}")
    print(f"   f(x)            = {f}")
    print(f"   integral        = {float(integral):.4f}\n")