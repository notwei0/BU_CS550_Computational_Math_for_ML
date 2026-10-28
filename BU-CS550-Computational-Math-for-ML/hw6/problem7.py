import sympy as sp

x, y, lam = sp.symbols("x y lambda", real=True)

f = x**2 + 2*y**2
g = x - 2*y + 1

#Lagrangian
#L = f(x,y) - lambda * g(x,y) =  x^2 + 2y^2 - lambda*(x - 2y + 1)
L = f - lam*g
print("a) L =", L)

#gradient of L (w.r.t. x, y, lambda)
#dL/dx = 2x - lambda
#dL/dy = 4y + 2*lambda
#dL/dlambda = -(x - 2y + 1)
dLdx = sp.diff(L, x)
dLdy = sp.diff(L, y)
dLdlam = sp.diff(L, lam)
print("grad L =", (dLdx, dLdy, dLdlam))

#set grad L = 0
#2x - lambda = 0
#4y + 2*lambda = 0
#x - 2y + 1 = 0
print("equations:")
print(sp.Eq(dLdx, 0))
print(sp.Eq(dLdy, 0))
print(sp.Eq(dLdlam, 0))

#by hand:
#from eq1: lambda = 2x
#sub into eq2: 4y + 2(2x) = 0 -> 4y + 4x = 0 -> y = -x
#sub into eq3: x - 2(-x) + 1 = 0 -> x + 2x + 1 = 0 -> 3x = -1 -> x = -1/3
#y = -x = 1/3
#f(x,y) = x^2 + 2y^2 = (1/3)^2 + 2(1/3)^2 = 1/9 + 2/9 = 3/9 = 1/3
sol = sp.solve([dLdx, dLdy, dLdlam], [x, y, lam])
print("d) solution:", sol)
min_val = f.subs({x: sol[x], y: sol[y]})
print("   f(x,y) at this point =", min_val)