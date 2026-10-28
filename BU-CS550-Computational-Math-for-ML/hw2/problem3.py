import sympy as sym
from colorama import Fore

#symbols and values
x = sym.symbols('x')
n = 3
x_value = 5
delta_x = 0.1

#10 functions from Problem 1 (only f is written down)
problem3 = [
    ("1",  sym.Integer(2)),
    ("2",  x**2),
    ("3",  2*x**2 + x),
    ("4",  x**n + n),
    ("5",  2*sym.sqrt(x)),
    ("6",  sym.exp(x + 1)),
    ("7",  sym.Integer(3)**x),
    ("8",  sym.log(x) + 1),
    ("9",  sym.sin(x + sym.pi/6)),
    ("10", sym.cos(x + sym.pi/6)),
]

#find the derivative and f'(x=1) of each function and creates a table
print(f"{'f(x)':<25} {'forward':<12} {'backward':<12} {'central':<12} {'exact':<10}")

for label, f in problem3:
    fprime = sym.simplify(sym.diff(f, x))
    exact = fprime.subs(x, x_value)

    #finds the forward, backward, and central difference approximations of f'(x=1)
    forward = (f.subs(x, x_value + delta_x) - f.subs(x, x_value)) / delta_x
    backward = (f.subs(x, x_value) - f.subs(x, x_value - delta_x)) / delta_x
    central = (f.subs(x, x_value + delta_x) - f.subs(x, x_value - delta_x)) / (2 * delta_x)

    #find the difference between the exact and approximate values
    forward_diff = abs(exact - forward)
    backward_diff = abs(exact - backward)
    central_diff = abs(exact - central)

    #compares the values to see which approximation is closest and farthest to the exact value
    min_diff = min(forward_diff, backward_diff, central_diff)
    max_diff = max(forward_diff, backward_diff, central_diff)

    #colors the closest approximation to the exact value in green and the farthest in red
    if forward_diff == min_diff:
        forward_color = Fore.GREEN
    elif forward_diff == max_diff:
        forward_color = Fore.RED
    else:
        forward_color = Fore.RESET

    if backward_diff == min_diff:
        backward_color = Fore.GREEN
    elif backward_diff == max_diff:
        backward_color = Fore.RED
    else:
        backward_color = Fore.RESET

    if central_diff == min_diff:
        central_color = Fore.GREEN
    elif central_diff == max_diff:
        central_color = Fore.RED
    else:
        central_color = Fore.RESET

    #creates a table to organize the results
    print(f"{str(f):<25} {forward_color}{float(forward):<12.4f}{Fore.RESET} {backward_color}{float(backward):<12.4f}{Fore.RESET} {central_color}{float(central):<12.4f}{Fore.RESET} {float(exact):<10.4f}")

#report findings
print("the central values are the closest to the exact values for all functions except cos(x + pi/6) where the forward value is the closest to the exact value. Most likely from the nature of the central difference method which uses both forward and backward differences to calculate the derivative. The forward difference method is the closest to the exact value for cos(x + pi/6) because the function is decreasing at x=1, so the forward difference is a better approximation of the derivative than the central difference.")