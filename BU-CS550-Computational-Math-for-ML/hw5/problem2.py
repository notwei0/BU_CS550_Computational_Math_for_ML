import numpy as np
import matplotlib.pyplot as plt
#outside help told me to use comb 
from math import comb

# binomial probability formula
def bin(k, n, p):
    return comb(n, k) * p**k * (1-p)**(n-k)

p_val = np.linspace(0.5, 1, 200)
accuracy = 3 * p_val**2 - 2*p_val**3

# majority vote needs at least 2 out of 3 correct
# P(X>=2) = C(3,2)*p^2*(1-p) + C(3,3)*p^3 = 3p^2 - 2p^3
print("N=3 accuracy = 3p^2 - 2p^3")

#sets points in between 0.5 and 1
for p in [0.6, 0.7, 0.8, 0.9]:
    ensemble = 3*p**2 - 2*p**3
    verify = bin(2, 3, p) + bin(3, 3, p)
    print(f"p={p:.1f}: single={p:.4f}, ensemble={ensemble:.4f} (verify={verify:.4f})")

plt.figure(figsize=(10, 5))
plt.plot(p_val, p_val, "r--", label="Single classifier")
plt.plot(p_val, accuracy, "b-", label="N=3 (3p^2 - 2p^3")
plt.xlabel("Individual Classifier")
plt.ylabel("Accuracy")
plt.title("Problem 2")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()