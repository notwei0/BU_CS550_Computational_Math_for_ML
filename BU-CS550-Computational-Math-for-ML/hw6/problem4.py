import sympy as sp

#sets x as a variable thats real
x = sp.symbols("x", real=True)

#makes a list of the expressions
problem4 = [
    ("x^2 - 5",                     x**2 - 5),
    ("x^3 - 5",                     x**3 - 5),
    ("sqrt(x) - 1.5",               sp.sqrt(x) - sp.Rational(3, 2)),
    ("e^x - 2",                     sp.exp(x) - 2),
    ("2^x - 0.5",                   2**x - sp.Rational(1, 2)),
    ("log(x) - 1",                  sp.log(x) - 1),
    ("sin(x) - 0.5",                sp.sin(x) - sp.Rational(1, 2)),
    ("cos(x) - 0.5",                sp.cos(x) - sp.Rational(1, 2)),
]

#for loop to find the expressions
for name, expr in problem4:
    roots = sp.solve(expr, x)
    print(name)
    print("f(x) =", expr)
    print("roots:", roots)
    for r in roots:
        print(r, "=", sp.N(r))
    print()