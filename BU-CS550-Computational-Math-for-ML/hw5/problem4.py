import numpy as np
#recieved heavy help from a friend who codes in python
X = np.arange(0, 100)

# P(X >= 25)
a = np.sum(X >= 25) / 100
print(f"a) P(X >= 25):  values = {np.sum(X >= 25)}/100 = {a:.4f}")

#P(2.5 < X < 12.5)
b = np.sum((X > 2.5) & (X < 12.5)) / 100
print(f"b) P(2.5 < X < 12.5):  values = {np.sum((X > 2.5) & (X < 12.5))}/100 = {b:.4f}")

# P(8 < X <= 10 or 30 < X <= 32) - mutually exclusive
A = (X > 8)  & (X <= 10)
B = (X > 30) & (X <= 32)
c = np.sum(A | B) / 100
print(f"P(8<X<=10 or 30<X<=32):  {np.sum(A)} + {np.sum(B)} = {np.sum(A|B)}/100 = {c:.4f}")
print(f"Mutually exclusive: P(A)+P(B) = {np.sum(A)/100:.2f} + {np.sum(B)/100:.2f} = {c:.4f}")

# P(50 < X <= 70 or 60 < X <= 80) - overlapping
C = (X > 50) & (X <= 70)
D = (X > 60) & (X <= 80)
intersection = np.sum(C & D)
d = np.sum(C | D) / 100
print(f"P(50<X<=70 or 60<X<=80):")
print(f"P(A)={np.sum(C)/100:.2f}, P(B)={np.sum(D)/100:.2f}, P(AnB)={intersection}/100={intersection/100:.2f}")
print(f"P(AUB) = {np.sum(C)/100:.2f} + {np.sum(D)/100:.2f} - {intersection/100:.2f} = {d:.4f}")