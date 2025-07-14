# Modèle Cosmologique Fractal : Unification par Antagonisme et Structure de Fibonacci v1.2.2

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15863407.svg)](https://doi.org/10.5281/zenodo.15863407)

## 📜 Résumé

Ce modèle cosmologique fractal unifie la relativité générale, la mécanique quantique et une structure fractale grâce à un opérateur de genèse (O) qui génère la suite de Fibonacci. Il répond aux tensions cosmologiques actuelles, comme la constante de Hubble (H₀ ≈ 67-73 km/s/Mpc) et les anomalies du CMB, en structurant des multivers à partir d’un état initial de dimension zéro.

**Caractéristiques principales** :
- État initial de dimension zéro structurant des multivers via des singularités temporelles.
- Couplage observateur-métrique intégrant l’observateur.
- Réduction des anomalies : χ² réduit de 81,63 % (p = 0,002, 3σ) par rapport à ΛCDM.
- Prédictions testables avec Planck, CMB-S4 et Euclid.

## 🔍 Contenu du Répertoire

- `main.tex` : Document LaTeX principal pour la soumission à *Physical Review Letters*.
- `figures/` : Répertoire contenant les figures (ex. : convergence de la dimension fractale, spectre CMB).
- `scripts/` :
  - `cmb_chi2_calculation.py` : Calcule χ² pour le spectre de puissance CMB (Planck 2018).
  - `galaxy_correlation_evolution.py` : Analyse la corrélation des galaxies avec l’évolution du redshift.
- `Fractal_Cosmological_Model.pdf` : Manuscrit compilé.
- `.zenodo.json` : Métadonnées pour Zenodo.
- `CITATION.cff` : Métadonnées de citation.

## 🧪 Prédictions Testables

1. Indice de puissance CMB : α ≈ 1,618 ± 0,1.
2. Pente de corrélation des galaxies : γ(z) ≈ 1,382 + 0,36 log(1 + z) ± 0,1.
3. Variation des constantes fondamentales : δφ ~ 10⁻⁵.

## 📊 Équations Clés

### Opérateur de Genèse
O |ψₙ⟩ = Fₙ |ψₙ⟩, où Fₙ = Fₙ₋₁ + Fₙ₋₂, F₀ = 1, F₁ = -1

### Dimension Fractale
dim_F(Uₙ) ≈ φ ≈ 1,618

### Lagrangien
Lₙ = √(-g) [R/(16πG) + φ ⟨ψₙ|O|ψₙ⟩]

## 📚 Comment Citer

```bibtex
@software{Herbin_Fractal_Cosmological_Model_2024,
  author = {Herbin, Sylvain},
  orcid = {0009-0001-3390-5012},
  title = {{Modèle Cosmologique Fractal : Unification par Antagonisme et Structure de Fibonacci}},
  month = jul,
  year = 2024,
  publisher = {Zenodo},
  version = {1.0},
  doi = {10.5281/zenodo.15863407},
  url = {https://doi.org/10.5281/zenodo.15863407}
}
```
## ⚖️ License

This project is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## 🛠️ Usage

1. **Compile the Manuscript**:
   - Ensure a LaTeX distribution (e.g., TeXlive, MikTeX) is installed.
   - Run `pdflatex main.tex` to compile the PDF.
   - Figures are located in the `figures/` directory.

2. **Run the Scripts**:
   - The Python scripts (`cmb_chi2_calculation.py`, `galaxy_correlation_evolution.py`) require Python 3.x with `numpy`, `matplotlib`, and `scipy`.
   - Check the scripts for specific dependencies.

## 📬 Contact

For questions, contact Sylvain Herbin at [herbinsylvain@protonmail.com](mailto:herbinsylvain@protonmail.com). ORCID: [0009-0001-3390-5012](https://orcid.org/0009-0001-3390-5012).
