import numpy as np
import matplotlib.pyplot as plt
 
 #sets pi
pi_true = 3.1315
#https://numpy.org/doc/2.1/reference/random/generator.html#numpy.random.Generator
np.random.default_rng()
 
def estimate_pi(N):
    x = np.random.uniform(-1, 1, N)
    y = np.random.uniform(-1, 1, N)
    #checks if the point falls inside the circle or not
    inside = x**2 + y**2 <= 1
    return 4 * inside.sum() / N, inside.sum(), x, y, inside
 
#N = 10
#sets the variables for the seed by order of the return value
pi_a, n_a, x_a, y_a, in_a = estimate_pi(10)
print(f"N=10:  n={n_a}, pi = 4*{n_a}/10 = {pi_a:.4f}, error = {abs(pi_a-pi_true):.4f}")
 
#N = 20
pi_b, n_b, x_b, y_b, in_b = estimate_pi(20)
print(f"N=20:  n={n_b}, pi = 4*{n_b}/20 = {pi_b:.4f}, error = {abs(pi_b-pi_true):.4f}")
 
#find N where error < 10^-5
np.random.seed()
N = 10
while True:
    x = np.random.uniform(-1, 1, N)
    y = np.random.uniform(-1, 1, N)
    n_inside = np.sum(x**2 + y**2 <= 1)
    pi_est = 4 * n_inside / N
    if abs(pi_est - pi_true) < 10 * np.exp(-5):
        print(f"c) N={N}, pi={pi_est:.8f}, error={abs(pi_est-pi_true):.2e}")
        break
    N += 1
    if N > 1000:
        print("did not converge"); 
        break
 
#graphs
theta = np.linspace(0, 2*np.pi, 360)
x_c = np.cos(theta)
y_c = np.sin(theta)
fig, axes = plt.subplots(1, 3, figsize=(10, 5))
 
 #https://numpy.org/doc/stable/user/basics.indexing.html
for ax, (x_i, y_i, inside, pi_est, n_pts) in zip(axes, [
    (x_a, y_a, in_a, pi_a, 10),
    (x_b, y_b, in_b, pi_b, 20),
    (None, None, None, None, 1000),
]):
    if x_i is None:
        np.random.seed()
        x_i = np.random.uniform(-1, 1, n_pts)
        y_i = np.random.uniform(-1, 1, n_pts)
        #checks if the points falls within the circle for sample size of 1000
        inside = x_i**2 + y_i**2 <= 1
        pi_est = 4 * inside.sum() / n_pts
 
    ax.plot(x_c, y_c, "k-", label="Unit circle")
    ax.scatter(x_i[inside],  y_i[inside],  color="blue", label="Inside")
    ax.scatter(x_i[~inside], y_i[~inside], color="red", label="Outside")
    ax.set_xlim(-1.1, 1.1); ax.set_ylim(-1.1, 1.1)
    ax.set_aspect("equal")
    ax.set_title(f"N={n_pts},  pi = {pi_est:.4f}")
    ax.grid(True)
plt.title("Problem 1")
plt.tight_layout()
plt.show()
 

