import numpy as np
import matplotlib.pyplot as plt
import os

def fractal_dimension(n_max, lambda_scale=1.346):
    fib_pos = [0, 1]  # Branche positive : 0, 1, 1, 2, 3, 5, ...
    fib_neg = [0, -1]  # Branche négative : 0, -1, -1, -2, -3, -5, ...
    dimensions = []
    
    for i in range(1, n_max - 1):
        fib_pos.append(fib_pos[i] + fib_pos[i-1])
        fib_neg.append(fib_neg[i] + fib_neg[i-1])
        if i > 1 and fib_pos[i] != 0 and fib_pos[i-1] != 0:
            ratio = abs(fib_pos[i] / fib_pos[i-1])
            dim = np.log(ratio) / np.log(lambda_scale)
            dimensions.append(dim)
        else:
            dimensions.append(np.nan)
    
    return range(2, n_max), dimensions

n_max = 20  # Réduit pour lisibilité
lambda_scale = 1.346
x, dimensions = fractal_dimension(n_max, lambda_scale)

valid_data = [(i, d) for i, d in zip(x, dimensions) if not np.isnan(d)]
valid_x = [item[0] for item in valid_data]
valid_dimensions = [item[1] for item in valid_data]

os.makedirs("figures", exist_ok=True)

plt.figure(figsize=(10, 6), dpi=300)  # Ajusté pour clarté
plt.plot(valid_x, valid_dimensions, label=r"Fractal dimension $\dim_{\mathscr{F}}(\mathcal{U}_n)$", color="blue", linewidth=2)
plt.axhline(y=1.61803398875, color="red", linestyle="--", label=r"$\phi \approx 1.618$")
plt.xlabel("n", fontsize=12)
plt.ylabel("Fractal Dimension", fontsize=12)
plt.legend(fontsize=10)
plt.grid(True)
plt.savefig("figures/fractal_dimension.png")
plt.show()
