import numpy as np
#recieved heavy help from a friend who codes in python
lam = 1.0

# Monte Carlo verification
np.random.seed()
N = 1000000
T1 = np.random.exponential(1/lam, N)
T2 = np.random.exponential(1/lam, N)
mc_prob = np.mean(T1 >= 2 * T2)

print("By hand:")
print("Inner integral: integral from 2t2 to inf of lam*e^(-lam*t1) dt1 = e^(-2*lam*t2)")
print("Outer integral: integral from 0 to inf of e^(-2*lam*t2) * lam*e^(-lam*t2) dt2")
print("lam * integral from 0 to inf of e^(-3*lam*t2) dt2")
print("lam * 1/(3*lam)")
print(f"Analytical answer: {1/3:.6f}")
print(f"Monte Carlo verification: {mc_prob:.6f}")