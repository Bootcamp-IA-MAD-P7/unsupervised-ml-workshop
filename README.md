<div align="center">

# Unsupervised ML Workshop

### Machine Learning Bootcamp · Gaby Granja

Dimensionality Reduction • Clustering • Anomaly Detection

<br>

![Python](https://img.shields.io/badge/Python-3.13-black?style=for-the-badge&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-black?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-black?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-black?style=for-the-badge&logo=numpy&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-black?style=for-the-badge&logo=jupyter&logoColor=white)
![Git](https://img.shields.io/badge/Git-black?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-black?style=for-the-badge&logo=github&logoColor=white)

<br>

![Status](https://img.shields.io/badge/Status-Active%20Development-white?style=flat-square&labelColor=black)
![Bootcamp](https://img.shields.io/badge/Bootcamp-AI%20MAD%20P7-white?style=flat-square&labelColor=black)
![Version](https://img.shields.io/badge/Version-v0.2-white?style=flat-square&labelColor=black)

</div>

---

> [!IMPORTANT]
>
> This repository documents my learning journey through the Unsupervised Machine Learning module of the AI Bootcamp.
>
> Every notebook follows a reproducible workflow combining data preprocessing, dimensionality reduction, clustering, visualization and anomaly detection.

---

# Overview

This repository explores the practical application of **Unsupervised Machine Learning** using two complementary datasets with very different characteristics.

The objective is to understand how preprocessing, dimensionality reduction and clustering algorithms behave depending on the structure of the data, while documenting the complete analytical workflow.

Current work focuses on:

- Dimensionality Reduction (PCA & t-SNE)
- Clustering
- Cluster Validation
- Anomaly Detection
- Practical interpretation of results

---

# Scientific Report

The [MkDocs scientific report](docs/index.md) presents the advanced mushroom
study as a reproducible academic case study for educational and portfolio
purposes. It is not a peer-reviewed publication and must not be used as
real-world mushroom-safety guidance.

- [Read the report source](docs/index.md)
- [Open the advanced notebook](workshop-advanced-unsupervised.ipynb)

---

# Repository Structure

```text
.
├── data/
│   ├── mushrooms.csv
│   └── credit_card.csv
│
├── docs/
│   ├── daily/
│   ├── decisions.md
│   ├── methodology.md
│   ├── notebook-spec.md
│   ├── project-plan.md
│   └── ...
│
├── workshop-clustering-Mushrooms.ipynb
├── workshop-clustering-creditcard.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Development Status

| Module | Status |
|-------------------------------|:------:|
| Repository setup | ✅ |
| Development environment | ✅ |
| Documentation structure | ✅ |
| Mushroom Workshop | 🚧 |
| Credit Card Workshop | ⏳ |
| Final Documentation | ⏳ |

---

# Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- Scikit-learn
- Jupyter Notebook
- Git
- GitHub

---

# Implemented Algorithms

## Dimensionality Reduction

- PCA
- t-SNE

## Clustering

- K-Means
- Agglomerative Clustering
- Gaussian Mixture Models (GMM)
- DBSCAN

## Validation Metrics

- Silhouette Score
- Davies-Bouldin Index
- Calinski-Harabasz Score
- Adjusted Rand Index (ARI)
- Normalized Mutual Information (NMI)

## Anomaly Detection

- Isolation Forest

---

# Roadmap

## Mushroom Workshop

- [x] Dataset understanding
- [x] Data quality assessment
- [x] Missing value handling
- [x] Feature encoding
- [x] Train/Test split
- [x] PCA
- [x] t-SNE
- [x] Random Forest baseline
- [x] Clustering algorithms
- [x] Cluster validation
- [x] Isolation Forest
- [ ] Final review

## Credit Card Workshop

- [ ] Data understanding
- [ ] Exploratory Data Analysis
- [ ] Feature Scaling
- [ ] PCA
- [ ] Clustering
- [ ] Customer Segmentation
- [ ] Anomaly Detection

---

# Getting Started

Clone the repository

```bash
git clone https://github.com/Bootcamp-IA-MAD-P7/unsupervised-ml-workshop.git
```

Create the virtual environment

```bash
python -m venv .venv
```

Activate it

```bash
source .venv/Scripts/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Current Progress

## Completed

- Data quality assessment
- Missing value treatment
- One-Hot Encoding
- PCA
- t-SNE
- Random Forest baseline
- K-Means
- Agglomerative Clustering
- Gaussian Mixture Models
- DBSCAN
- Isolation Forest
- Internal and external clustering evaluation

## Next

- Final notebook review
- Documentation polishing
- Credit Card workshop

---

# Project Soundtrack

> Every project deserves its own soundtrack.

**Radiohead — From The Basement**

---

<div align="center">

Machine Learning Bootcamp · 2026

Developed by **Gaby Granja**

*"Good documentation is part of the product."*

</div>
