# Unsupervised ML Workshop

**Machine Learning Bootcamp · Gaby Granja**

**Dimensionality Reduction • Clustering • Association Rules • Knowledge Discovery**

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-Machine%20Learning-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Bootcamp](https://img.shields.io/badge/Academic-Bootcamp-lightgrey)

---

## Overview

This repository documents my work throughout the **Machine Learning Bootcamp**, exploring the practical application of **Unsupervised Machine Learning** using multiple real-world datasets.

The project focuses on discovering hidden structures, natural groupings and meaningful associations in unlabeled data through dimensionality reduction, clustering and knowledge discovery techniques.

Beyond implementing algorithms, this repository also emphasizes reproducibility, technical documentation and professional project presentation.

---

# Project Website

As part of this project, I am also building a **research-style project website** to practice how Machine Learning studies are commonly documented and presented.

The website summarizes the methodology, experiments, visualizations and key findings, while the Jupyter notebooks remain the reproducible technical implementation.

### Live Project Website

**https://bootcamp-ia-mad-p7.github.io/unsupervised-ml-workshop/**

Current contents include:

- Project overview
- Methodology
- Experiments
- Results
- Discussion
- Conclusions
- References
- Interactive visualizations

---

# Project Highlights

### Dimensionality Reduction

- Principal Component Analysis (PCA)
- Uniform Manifold Approximation and Projection (UMAP)

### Clustering

- K-Means
- HDBSCAN

### Knowledge Discovery

- FP-Growth
- Association Rule Mining

### Evaluation

- Adjusted Rand Index (ARI)
- Normalized Mutual Information (NMI)
- Cluster comparison
- Parameter sensitivity analysis

---

# Visualizations

The project includes multiple visual analyses, including:

- PCA Projection
- UMAP Projection
- K-Means vs Ground Truth
- HDBSCAN Parameter Sensitivity
- Feature Frequency Comparison
- Dumbbell Plot
- Feature Heatmap
- Association Network
- Interactive Sankey Diagram

---

# Repository Structure

```text
.
├── data/
│   ├── mushrooms.csv
│   └── credit_card.csv
│
├── docs/
│   ├── paper/
│   ├── figures/
│   └── assets/
│
├── scripts/
│
├── workshop-clustering-mushrooms.ipynb
├── workshop-advanced-unsupervised.ipynb
├── workshop-clustering-creditcard.ipynb
│
├── mkdocs.yml
├── requirements.txt
├── requirements-docs.txt
│
└── README.md
```

---

# Development Status

| Module | Status |
|---------|:------:|
| Repository setup | ✅ |
| Git workflow | ✅ |
| Mushroom Workshop | ✅ |
| Advanced Unsupervised Workshop | ✅ |
| Research-style Website | ✅ |
| Documentation | ✅ |
| Credit Card Workshop | 🚧 |

---

# Technical Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- SciPy
- Matplotlib
- Plotly
- UMAP
- HDBSCAN
- mlxtend
- Jupyter Notebook
- MkDocs Material
- Git
- GitHub

---

# Reproducibility

Clone the repository:

```bash
git clone https://github.com/Bootcamp-IA-MAD-P7/unsupervised-ml-workshop.git
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

```bash
source .venv/Scripts/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Build the documentation:

```bash
mkdocs build --strict
```

Serve the website locally:

```bash
mkdocs serve
```

---

# Current Roadmap

### Completed

- Repository setup
- Development environment
- Git workflow
- Mushroom clustering workshop
- Advanced unsupervised learning notebook
- UMAP dimensionality reduction
- HDBSCAN clustering
- Association Rule Mining
- Interactive visualizations
- Research-style documentation website

### In Progress

- Credit Card customer segmentation
- Additional clustering comparisons
- Final project refinements

---

# Academic Note

This repository was developed as part of a **Machine Learning Bootcamp**.

The project includes a **research-style website** created as a learning exercise to practice the structure, communication and visualization commonly found in technical and academic publications.

It is **not** a peer-reviewed scientific publication.

The mushroom analyses and association rules are intended exclusively for educational purposes and must **never** be interpreted as guidance for real-world mushroom identification or consumption.

---

# Project Soundtrack

Every project deserves its own soundtrack.

**Radiohead — From The Basement**

---

Developed by **Gaby Granja**

*"Good documentation is part of the product."*