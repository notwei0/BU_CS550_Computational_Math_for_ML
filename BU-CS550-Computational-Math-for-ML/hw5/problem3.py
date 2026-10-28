import numpy as np
import matplotlib.pyplot as plt

#recieved heavy help from a friend who codes in python
 
#build the sum table from two dice
sums = []
for d1 in range(1, 7):
    for d2 in range(1, 7):
        sums.append(d1 + d2)
 
# X = +sum if odd, -sum if even
X_values = [s if s % 2 != 0 else -s for s in sums]
 
# probability distribution table (ai was used to create an even table)
unique_x = sorted(set(X_values))
probs = [X_values.count(x) / 36 for x in unique_x]
 
print("a) Probability Distribution Table for X:")
print(f"{"X":>5} | {"Ways":>5} | {"P(X)":>8}") #ai was used here to make the lines show up correctly
print("-" * 25)
for x, p in zip(unique_x, probs):
    ways = int(p * 36)
    print(f"{x:>5} | {ways:>5} | {ways}/36 = {p:.4f}") #same thing here
 
# expected value
EX = sum(x * p for x, p in zip(unique_x, probs))
print(f"\nb) E(X) = sum of x * P(x)")
print(f"       = (1/36) * [{" + ".join(str(x * int(p*36)) for x, p in zip(unique_x, probs))}]")
print(f"       = (1/36) * {sum(x * int(p*36) for x, p in zip(unique_x, probs))}")
print(f"       = {EX:.4f}")
 
# plots points
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
 
axes[0].bar(unique_x, probs, color=["red" if x < 0 else "blue" for x in unique_x], alpha=0.7)
axes[0].set_xlabel("X (dollars won/lost)")
axes[0].set_ylabel("P(X)")
axes[0].set_title("Probability Distribution of X")
axes[0].axvline(0, color="k", lw=0.5)
axes[0].grid(True, alpha=0.3)
axes[0].legend(handles=[
    plt.Rectangle((0,0),1,1, color="blue", alpha=0.7, label="Win (odd sum)"),
    plt.Rectangle((0,0),1,1, color="red",  alpha=0.7, label="Lose (even sum)")
])
 
# Sum frequency from dice
sum_counts = {s: sums.count(s) for s in range(2, 13)}
colors = ["red" if s % 2 == 0 else "blue" for s in sum_counts]
axes[1].bar(sum_counts.keys(), sum_counts.values(), color=colors, alpha=0.7)
axes[1].set_xlabel("Dice Sum")
axes[1].set_ylabel("Number of Ways")
axes[1].set_title("Dice Sum Frequency (blue=odd/win, red=even/lose)")
axes[1].grid(True, alpha=0.3)
 
plt.suptitle("Problem 3 - Two Dice Win/Lose Game", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.show()