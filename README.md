# The Dynamic Fractal Cosmological Model: Formalism and Key Predictions v1.4.0

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15973540.svg)](https://doi.org/10.5281/zenodo.15973540)
Visit our website: [www.phi-z.space](https://www.phi-z.space)

---

## 📜 Abstract

This repository presents **v1.4.0** of the **Dynamic Fractal Cosmological Model**, a novel framework that introduces an evolving effective spacetime dimension, $\phi(z)$, to address major cosmological tensions. Unlike the standard $\Lambda$CDM, our model modifies the Universe's expansion history and the growth of large-scale structures by incorporating an exponential transition, an oscillation, and a Gaussian feature within $\phi(z)$.

**Key Achievements & Features**:
- **Hubble Tension Resolved**: Achieves a best-fit Hubble constant of $H_0 = 73.24 \pm 0.42$ km/s/Mpc, aligning with local SH0ES measurements at a remarkable **$0.3\sigma$ agreement**.
- **Unprecedented Goodness-of-Fit**: Boasts a combined $\chi^2/\text{dof} = 0.951$ for selected datasets (BAO, CMB, Galaxy 2PCF, Cluster Mass Function), representing a significant **$7.1\sigma$ improvement over $\Lambda$CDM**.
- **Lithium-7 Problem**: Demonstrates consistency with primordial abundances within **$1.8\sigma$**, attributed to a decoupled primordial fractal dimension ($\phi_{\text{BBN}} = 2.970$).
- **Dynamic Dark Energy**: Introduces a redshift-dependent dark energy equation of state $w_{\Lambda}(z) = -1 + 0.2(\phi(z) - 1.618)$.
- **Novel Dark Matter-Baryon Coupling**: Features a new interaction term $\frac{d\rho_c}{dt} + 3H\rho_c = -\beta \phi(z) H \rho_b$, with $\beta = 4.7 \times 10^{-5}$.
- **Predictive Power**: Offers concrete, testable predictions for future surveys like Euclid, Roman HLS, and DESI-II.

---

## 🔍 Repository Contents

- `main.tex`: The primary LaTeX document for the manuscript.
- `figures/`: Contains all figures, including the optimized $\phi(z)$ evolution, $H(z)$ comparison, Hubble tension resolution, CMB spectrum, and cluster mass function.
- `phiz_data.dat`: Data table containing the precomputed $\phi(z)$ values, including the BBN correction point.
- `methods/`: Directory for supplementary methodology documents (e.g., `Expansion_History.pdf`, `BAO.pdf`, `physical_justification_phi_z_bumps.pdf`).
- `Fractal_Cosmological_Model.pdf`: The compiled manuscript.
- `.zenodo.json`: Metadata file for Zenodo.
- `CITATION.cff`: Citation metadata.

---

## 🧪 Testable Predictions for Next-Generation Surveys

Our model generates distinctive observational signatures detectable with upcoming missions:

1.  **Matter Power Spectrum Deviations**: Predicted deviations in $P_{\text{fractal}}(k,z)/P_{\Lambda\text{CDM}}(k,z) = (\phi(z)/1.62)^{1.8} e^{-(k/0.02)^2}$:
    | Survey         | Redshift Range | k-range [h/Mpc] | Deviation           |
    | :------------- | :------------- | :-------------- | :------------------ |
    | Euclid (spectro) | 0.9-1.8        | 0.005-0.1       | +8.2% $\pm$ 0.9%    |
    | Roman HLS      | 1.5-2.8        | 0.003-0.05      | +12.7% $\pm$ 1.2%   |
    | DESI-II        | 2.5-4.0        | 0.001-0.03      | +18.3% $\pm$ 2.1%   |

2.  **CMB Spectral $\mu$-distortions**: Predicted $\mu = (1.7 \pm 0.3) \times 10^{-8}$ (detectable at $2\sigma$ with PIXIE) from the fractal phase transition at $z \sim 10^4$.

---

## 📊 Key Equations

### Dynamic Fractal Dimension $\phi(z)$
$$\phi(z) = \phi_{\infty} + (\phi_0 - \phi_{\infty}) e^{-\Gamma z} + A_1 e^{-0.5((z - 0.4)/0.3)^2} + A_2 e^{-0.5((z - 1.5)/0.4)^2}$$
*With additional oscillation and a Gaussian feature specifically at $z=1.5$ for BAO fitting, as depicted in figures.*

### Modified Friedmann Equation (Spatially Flat)
$$H^2(z) = H_0^2\left[\Omega_m(1+z)^{3\phi(z)} + \Omega_\Lambda(1+z)^{3(2-\phi(z))}\right]$$

### Dynamic Dark Energy Equation of State
$$w_{\Lambda}(z) = -1 + 0.2(\phi(z) - 1.618)$$

### Dark Matter-Baryon Coupling
$$\frac{d\rho_c}{dt} + 3H\rho_c = -\beta \phi(z) H \rho_b   \quad \beta = 4.7 \times 10^{-5}$$

---

## 📚 How to Cite

```bibtex
@software{Herbin_Dynamic_Fractal_Cosmological_Model_2024,
  author = {Herbin, Sylvain},
  orcid = {0009-0001-3390-5012},
  title = {{The Dynamic Fractal Cosmological Model: Formalism and Key Predictions}},
  month = jul,
  year = 2024,
  publisher = {Zenodo},
  version = {1.4.0},
  doi = {10.5281/zenodo.15973540},
  url = {[https://doi.org/10.5281/zenodo.15973540](https://doi.org/10.5281/zenodo.15973540)}
}
