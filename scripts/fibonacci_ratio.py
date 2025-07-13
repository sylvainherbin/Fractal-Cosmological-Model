import numpy as np
import matplotlib.pyplot as plt

def fibonacci_ratio(n_max):
    fib = [1, -1, 0]  # F_0 = 1, F_1 = -1, F_2 = 0
    ratios = []
    for i in range(3, n_max):
        fib.append(fib[i-1] + fib[i-2])
        if fib[i-1] != 0:  # Éviter la division par zéro
            ratios.append(abs(fib[i] / fib[i-1]))
        else:
            ratios.append(np.nan)  # Insérer NaN si division par zéro
    return range(3, n_max), ratios

n_max = 20
x, ratios = fibonacci_ratio(n_max)
plt.plot(x, ratios, label=r"Ratio $|F_{n}/F_{n-1}|$", color="blue")
plt.axhline(y=1.61803398875, color="red", linestyle="--", label=r"$\phi \approx 1.618$")
plt.xlabel("n")
plt.ylabel("Ratio")
plt.legend()
plt.grid(True)
plt.savefig("fibonacci_ratio.png")
plt.show()
