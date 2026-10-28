import sympy as sym

#symbols
x = sym.symbols('x')
y = sym.symbols('y')
n = 3

#10 functions from Problem 1 (only f is written down)
problem2 = [
    ("1",  sym.Integer(2)),
    ("2",  sym.exp(x**2)),
    ("3",  2*x**2 + x),
    ("4",  x**n + n),
    ("5",  2*sym.sqrt(x)),
    ("6",  sym.exp(x + 1)),
    ("7",  sym.Integer(3)**x),
    ("8",  sym.log(x) + 1),
    ("9",  sym.sin(x + sym.pi/6)),
    ("10", sym.cos(x + sym.pi/6)),
]

for label, f in problem2:
    #differentiation:  sym.diff(func, var)
    fprime = sym.simplify(sym.diff(f, x))

    #verification with the limit definition
    limit_check = sym.limit((f.subs(x, x + y) - f) / y, y, 0)
    agrees = sym.simplify(fprime - limit_check) == 0

    print(f"#{label}")
    print(f"   f(x)            = {f}")
    print(f"   sym.diff        = {fprime}")
    print(f"   limit check     = {limit_check}"
          f"   -> {'agrees' if agrees else 'differs'}")
    print(f"   f(1) = {f.subs(x, 1)},  f'(1) = {fprime.subs(x, 1)}\n")