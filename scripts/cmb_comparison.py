import numpy as np
import matplotlib.pyplot as plt
import os

# Désactiver l'utilisation de LaTeX externe et utiliser le rendu natif
plt.rc("text", usetex=False)
plt.rc("font", family="serif", size=12)

# Réinitialisation du canevas
plt.clf()
plt.close("all")

# Chargement des données Planck 2018
data = np.loadtxt("data/COM_PowerSpect_CMB-TT-full_R3.01.txt")
l = data[:, 0]  # Multipoles
dl_planck = data[:, 1]  # D_l
cl_planck = dl_planck * 2 * np.pi / (l * (l + 1))  # Conversion to C_l

# Modèle fractal avec alpha = 1.618
alpha_fractal = 1.618
cl_fractal = 1e-10 * l ** (-alpha_fractal)
cl_fractal *= cl_planck[10] / cl_fractal[10]  # Ajustement à l=10

# Modèle LambdaCDM avec alpha ≈ 1.0
alpha_lcdm = 1.0
cl_lcdm = 1e-10 * l ** (-alpha_lcdm)
cl_lcdm *= cl_planck[10] / cl_lcdm[10]

# Création d'une nouvelle figure
plt.figure(figsize=(10, 6), dpi=300, frameon=False)
plt.plot(l, cl_planck, label="Planck 2018 Data", color="black", linewidth=1)
plt.plot(l, cl_fractal, label=f"Fractal Model (α = {alpha_fractal})", color="blue", linewidth=2)
plt.plot(l, cl_lcdm, label=f"ΛCDM (α = {alpha_lcdm})", color="red", linewidth=2)
plt.xlabel("Multipole l")
plt.ylabel("Power Spectrum C_l (µK²)")
plt.yscale("log")
plt.legend(loc="best")
plt.grid(True, which="both", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("figures/cmb_comparison.png", bbox_inches="tight", dpi=300)
plt.show()

# Téléchargement
from google.colab import files
files.download("figures/cmb_comparison.png")
