# scripts/galaxy_correlation_evolution.py
import numpy as np
import matplotlib.pyplot as plt
import os

# Paramètres
r = np.logspace(-1, 1.5, 100)  # Distance en h^-1 Mpc
z = np.linspace(0, 2, 100)  # Redshift de 0 à 2
gamma_base = 1.382  # Valeur de base
k = 0.36  # Coefficient d'évolution ajusté
r0 = 5.0  # Longueur de corrélation

# Dépendance gamma(z)
gamma_z = gamma_base + k * np.log(1 + z)
# Approximation xi(r) avec effet redshift
xi_fractal = (r0 / r[:, np.newaxis]) ** gamma_z

# Données SDSS (approximation)
xi_sdss = (r0 / r[:, np.newaxis]) ** 1.8

# Créer le dossier figures/ s'il n'existe pas
if not os.path.exists("figures"):
    os.makedirs("figures")

# Tracé
plt.figure(figsize=(8, 6), dpi=300)
for i in range(0, len(z), 10):  # Tracer pour z = 0, 0.2, ..., 2
    plt.loglog(r, xi_fractal[:, i], label=f"Fractal (z = {z[i]:.1f}, γ = {gamma_z[i]:.3f})", 
               color=plt.cm.viridis(i/len(z)), alpha=0.7, linewidth=1.5)
plt.loglog(r, xi_sdss[:, 0], label="SDSS (γ ≈ 1.8)", color="#FF6B6B", linewidth=2, linestyle="--")
plt.xlabel(r"Distance $r$ (h$^{-1}$ Mpc)")
plt.ylabel(r"Two-Point Correlation Function $\xi(r)$")
plt.title("Galaxy Two-Point Correlation Function with Enhanced Redshift Evolution")
plt.legend()
plt.grid(True, which="both", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("figures/galaxy_correlation_evolution_adjusted.png", bbox_inches="tight", dpi=300)
plt.show()

from google.colab import files
files.download("figures/galaxy_correlation_evolution_adjusted.png")
