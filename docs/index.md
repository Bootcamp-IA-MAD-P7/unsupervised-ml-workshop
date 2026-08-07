# Unsupervised Machine Learning Workshop

<p class="study-lede">Machine Learning Bootcamp · Gabriela Granja</p>

<div class="project-meta">
<strong>Author</strong><br>
Gabriela Granja<br>
Digital Marketing professional transitioning into Artificial Intelligence, Data Analytics and Machine Learning through hands-on technical projects.
</div>

This repository contains two complementary practical workshops for learning and
comparing unsupervised machine learning techniques on datasets with
fundamentally different structures. The notebooks are the reproducible evidence
of the analyses; this website presents the workflows, visualisations, results
and key learnings in a concise portfolio format.

## Two workshops

### Workshop 1 · Mushroom Dataset

A categorical dataset where sparse, high-dimensional representation is the
central challenge. The workflow moves from cleaning and One-Hot Encoding to
dimensionality reduction, centroid and density-based clustering, retrospective
evaluation, association rules and an advanced UMAP/HDBSCAN exploration.

[View Mushroom Workshop →](mushroom.md){ .md-button .md-button--primary }

### Workshop 2 · Credit Card Customer Segmentation

A numerical behavioural dataset with 8,950 customers and 17 modelling
variables after identifier removal. The workshop addresses missing values,
different numerical scales, skewed financial distributions, PCA, clustering,
customer profiling, anomaly detection and advanced representation and stability
analysis.

[View Credit Card Workshop →](credit-card.md){ .md-button .md-button--primary }

## Two datasets, different challenges

| Aspect | Mushroom Dataset | Credit Card Dataset |
|---|---|---|
| Data type | Categorical | Numerical |
| Main challenge | Sparse, high-dimensional representation | Scale, skewness and behavioural structure |
| Primary objective | Discover latent structure and readable associations | Identify interpretable customer segments |
| Preprocessing | Missing-category treatment, constant removal, One-Hot Encoding | Identifier removal, median imputation, StandardScaler |
| Dimensionality reduction | PCA, t-SNE and UMAP | PCA, t-SNE and UMAP |
| Clustering | K-Means, agglomerative, DBSCAN and HDBSCAN | K-Means, agglomerative, DBSCAN, Gaussian Mixture and HDBSCAN |
| Additional analysis | Association rules and anomaly exploration | Customer profiles, Isolation Forest and stability analysis |

## What this project explores

- Exploratory data analysis and preprocessing
- Scaling and representation choices
- PCA, t-SNE and UMAP
- K-Means, hierarchical clustering, DBSCAN and HDBSCAN
- Isolation Forest and association rules
- Internal and retrospective clustering metrics
- Sub-sampling stability analysis
- Clear interpretation of limitations and negative results

## Reproducibility

The project includes four executed notebooks: baseline and advanced workflows
for each dataset. Dependencies are declared in `requirements.txt`, random states
are fixed where applicable, and the notebooks were validated sequentially.
Website figures are exported from the recorded notebook outputs, while MkDocs
Material builds the documentation published on GitHub Pages.

[View the source repository](https://github.com/Bootcamp-IA-MAD-P7/unsupervised-ml-workshop){ .md-button }
