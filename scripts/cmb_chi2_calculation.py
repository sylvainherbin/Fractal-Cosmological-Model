# Script pour calculer le chi^2 du spectre de puissance CMB (Planck 2018)
import numpy as np
import matplotlib.pyplot as plt

# Désactiver l'utilisation de LaTeX externe pour compatibilité Colab
plt.rc("text", usetex=False)
plt.rc("font", family="serif", size=12)

# Réinitialiser les figures pour éviter les résidus
plt.clf()
plt.close("all")

# Charger les données Planck 2018
data = np.loadtxt("data/COM_PowerSpect_CMB-TT-full_R3.01.txt")
l = data[:, 0]  # Multipoles
dl_planck = data[:, 1]  # D_l
cl_planck = dl_planck * 2 * np.pi / (l * (l + 1))  # Conversion en C_l
sigma_l = data[:, 2] if data.shape[1] > 2 else 0.1 * cl_planck  # Erreurs (colonne 2 ou approximation)

# Filtrer pour l > 30 (focus sur la décroissance)
mask = l > 30
l = l[mask]
cl_planck = cl_planck[mask]
sigma_l = sigma_l[mask]

# Modèle fractal avec alpha = 1.618
alpha_fractal = 1.618
cl_fractal = 1e-10 * l ** (-alpha_fractal)
cl_fractal *= cl_planck[0] / cl_fractal[0]  # Normalisation au premier point

# Modèle LambdaCDM avec alpha ≈ 1.0
alpha_lcdm = 1.0
cl_lcdm = 1e-10 * l ** (-alpha_lcdm)
cl_lcdm *= cl_planck[0] / cl_lcdm[0]  # Normalisation au même point

# Calcul du chi^2
chi2_fractal = np.sum(((cl_planck - cl_fractal) ** 2) / (sigma_l ** 2))
chi2_lcdm = np.sum(((cl_planck - cl_lcdm) ** 2) / (sigma_l ** 2))
reduction_percent = ((chi2_lcdm - chi2_fractal) / chi2_lcdm * 100) if chi2_lcdm > 0 else 0

# Affichage des résultats
print(f"Chi^2 Fractal Model (l > 30): {chi2_fractal}")
print(f"Chi^2 LambdaCDM (l > 30): {chi2_lcdm}")
print(f"Reduction in Chi^2: {reduction_percent:.2f}%")

# Tracé pour vérification
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

# Téléchargement (pour Colab)
from google.colab import files
files.download("figures/cmb_comparison.png")
