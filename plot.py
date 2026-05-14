import pandas as pd
import matplotlib.pyplot as plt

dase = pd.read_csv("dase_convergence.csv")
random = pd.read_csv("random_convergence.csv")

plt.figure()
plt.plot(dase["generation"], dase["fitness"], label="DASE")
plt.plot(random["generation"], random["fitness"], linestyle="--", label="Random Baseline")

plt.xlabel("Generation")
plt.ylabel("Structural Fitness")
plt.ylim(0, 1)
plt.title("DASE vs Random Baseline")
plt.legend()
plt.grid(True)
plt.savefig("comparison.png")

print("Saved comparison.png")
