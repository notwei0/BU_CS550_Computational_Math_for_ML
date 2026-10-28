import numpy as np
import matplotlib.pyplot as plt
#recieved heavy help from a friend who codes in python

# sets variables
r   = 100    # number of heads needed
p   = 0.5   # fair coin
mu  = r / p       # mean total tosses = 200
var = r * (1-p) / p**2     # variance = 200
sig = np.sqrt(var)      # std dev = sqrt(200)

# z-score for 225 tosses
z = (225 - mu) / sig

# standard normal CDF approximation (no scipy needed)
from math import erfc, sqrt
prob = 0.5 * erfc(z / sqrt(2))

print("By hand:")
print(f"mu = r/p = {r}/{p} = {mu:.1f}")
print(f"var = r*(1-p)/p^2 = {r}*{1-p}/{p**2} = {var:.1f}")
print(f"sig = sqrt({var:.0f}) = {sig:.4f}")
print(f"z = (225 - {mu:.0f}) / {sig:.4f} = {z:.4f}")
print(f"P(X >= 225) = P(Z >= {z:.4f}) = 1 - Phi({z:.4f}) = {prob:.4f}")

#Monte Carlo verification
np.random.seed(42)
N = 100
count = 0
for _ in range(N):
    tosses = np.random.geometric(p, 100).sum()
    if tosses >= 225:
        count += 1
mc_prob = count / N
print(f"Monte Carlo verification: {mc_prob:.4f}")

#plot normal approximation
x = np.linspace(140, 260, 500)
normal_pdf = (1/(sig * np.sqrt(2*np.pi))) * np.exp(-0.5*((x-mu)/sig)**2)

plt.figure(figsize=(10, 5))
plt.plot(x, normal_pdf, "b-", lw=2, label="Normal approximation")
plt.fill_between(x, normal_pdf, where=(x >= 225), color="red", alpha=0.5, label=f"P(X>=225) = {prob:.4f}")
plt.axvline(225, color="r", linestyle="--")
plt.axvline(mu,  color="g", linestyle="--", label=f"mu = {mu:.0f}")
plt.xlabel("Total Tosses")
plt.ylabel("Density")
plt.title("Problem 7")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()