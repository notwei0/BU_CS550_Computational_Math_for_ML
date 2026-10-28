import sympy as sp
from scipy.optimize import minimize_scalar #found minimize_scalar in scipy docs with independent research

x = sp.symbols('x', real=True)

#f(x) = exp(-(x+1)^2)
#f'(x) = -2(x+1) * exp(-(x+1)^2)
#f'(x) = 0  ->  x = -1
#f(-1) = exp(0) = 1
#exp -(x+1)^2 <= 0 always, so 0 < f(x) <= 1
#x = -1 is actually a maximum (f = 1)
#as x -> +-inf, (x+1)^2 -> inf, so f(x) -> 0
#minimum exists, infimum = 0
f = sp.exp(-(x+1)**2)
df = sp.diff(f, x)
crit_f = sp.solve(df, x)
print("f(x) = exp(-(x+1)^2)")
print("f'(x) =", df)
print("critical points:", crit_f)
for c in crit_f:
    print("f(", c, ") =", f.subs(x, c))
print()

#g(x) = log(-(x+1)^2)
# by hand:
#-(x+1)^2 <= 0 for every real x (equals 0 only at x = -1)
#log of a non-positive number is undefined for real x
#at x = -1, argument = 0 -> log(0) -> -inf
#g has no real minimum, the function isn't real-valued anywhere
print("g(x) = log(-(x+1)^2)")
print("  domain is empty for real x (argument always <= 0)")
print("  no real minimum exists\n")

#h(x) = (x-2)^4 + (x-1)^2
# by hand:
# h'(x) = 4(x-2)^3 + 2(x-1)
# set h'(x) = 0 -> 4(x-2)^3 + 2(x-1) = 0
# no nice closed form, solve -> x ~ 1.41
# h(1.41) ~ 0.289 (this is a minimum since h -> inf as x -> +-inf)
h = (x-2)**4 + (x-1)**2
dh = sp.diff(h, x)
print("h(x) = (x-2)^4 + (x-1)^2")
print("  h'(x) =", dh)

crit_h = sp.nsolve(dh, x, 1.5)
print("critical point:", crit_h)
print("h(", crit_h, ") =", sp.N(h.subs(x, crit_h)))

# by python: scipy minimize_scalar
res = minimize_scalar(sp.lambdify(x, h))
print("minimized scalar: x =", res.x, ", h(x) =", res.fun)