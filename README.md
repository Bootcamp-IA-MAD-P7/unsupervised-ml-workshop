# Unsupervised Machine Learning Workshop

Machine Learning Bootcamp · Gabriela Granja

[![Project Website](https://img.shields.io/badge/Project-Website-black?style=for-the-badge)](https://bootcamp-ia-mad-p7.github.io/unsupervised-ml-workshop/)
[![Python](https://img.shields.io/badge/Python-3.11-black?style=flat-square)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-black?style=flat-square)](https://scikit-learn.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-black?style=flat-square)](https://jupyter.org/)
[![MkDocs](https://img.shields.io/badge/MkDocs-Material-black?style=flat-square)](https://www.mkdocs.org/)
![Status](https://img.shields.io/badge/Status-Bootcamp%20Project-black?style=flat-square)

Two practical workshops for learning how representation, preprocessing and
algorithm choice change unsupervised machine learning results. The executed
notebooks are the reproducible evidence; the
[GitHub Pages website](https://bootcamp-ia-mad-p7.github.io/unsupervised-ml-workshop/)
presents the workflows, visualisations, findings and limitations.

## Workshops

### 1. Mushroom Workshop

An 8,124-row categorical dataset becomes 115 One-Hot encoded features after
cleaning. The workshop compares PCA, t-SNE, UMAP, K-Means, agglomerative
clustering, DBSCAN and HDBSCAN, then uses FP-Growth association rules to recover
readable category combinations.

Key learning: visually organised embeddings do not necessarily produce
clusters that agree with the reference labels. Association rules offered the
clearest feature-level interpretation, while clustering results changed
materially with representation and density parameters.

[Read the Mushroom Workshop](https://bootcamp-ia-mad-p7.github.io/unsupervised-ml-workshop/mushroom/)

### 2. Credit Card Workshop

A numerical behavioural dataset contains 8,950 customers and 17 modelling
variables after identifier removal. The workflow covers median imputation,
StandardScaler, PCA, K-Means model selection, hierarchical clustering, DBSCAN,
Gaussian Mixture, customer profiling and Isolation Forest.

Key learning: three K-Means profiles provide the clearest baseline combination
of internal metrics and interpretability. Engineered KPIs and `log1p` produce a
more balanced but materially different segmentation, while UMAP/HDBSCAN reveals
an alternative six-cluster structure.

[Read the Credit Card Workshop](https://bootcamp-ia-mad-p7.github.io/unsupervised-ml-workshop/credit-card/)

## Reproducible notebooks

| Workshop | Baseline | Advanced |
|---|---|---|
| Mushroom | [`workshop-clustering-Mushrooms.ipynb`](workshop-clustering-Mushrooms.ipynb) | [`workshop-advanced-unsupervised.ipynb`](workshop-advanced-unsupervised.ipynb) |
| Credit card | [`workshop-clustering-creditcard.ipynb`](workshop-clustering-creditcard.ipynb) | [`workshop-clustering-creditcard-advanced.ipynb`](workshop-clustering-creditcard-advanced.ipynb) |

## Techniques applied

- Exploratory data analysis, missing-value treatment and feature scaling
- One-Hot Encoding, engineered ratios and `log1p` representation
- PCA, t-SNE and UMAP
- K-Means, hierarchical clustering, DBSCAN, Gaussian Mixture and HDBSCAN
- Silhouette, Calinski-Harabasz, Davies-Bouldin, ARI and NMI evaluation
- Isolation Forest anomaly exploration
- FP-Growth and association rule mining
- Sub-sampling stability analysis

## Repository structure

```text
.
├── data/
├── docs/
│   ├── assets/
│   └── figures/
├── scripts/
├── workshop-clustering-Mushrooms.ipynb
├── workshop-advanced-unsupervised.ipynb
├── workshop-clustering-creditcard.ipynb
├── workshop-clustering-creditcard-advanced.ipynb
├── mkdocs.yml
├── requirements.txt
├── requirements-docs.txt
└── README.md
```

## Run locally

```bash
git clone https://github.com/Bootcamp-IA-MAD-P7/unsupervised-ml-workshop.git
cd unsupervised-ml-workshop
python -m venv .venv
```

Activate the environment on Windows:

```powershell
.venv\Scripts\activate
```

Or on Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies and launch Jupyter:

```bash
pip install -r requirements.txt
jupyter notebook
```

Build the documentation:

```bash
pip install -r requirements-docs.txt
mkdocs build --strict
```

## Author

**Gabriela Granja**

Digital Marketing professional transitioning into Artificial Intelligence,
Data Analytics and Machine Learning through hands-on technical projects.
