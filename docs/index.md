# Advanced Unsupervised Learning Research Lab

<p class="study-lede">Academic Machine Learning case study · Mushroom dataset</p>

> **Academic disclosure**
>
> This report is a practical academic exercise developed during a Machine Learning Bootcamp. It follows a scientific-report structure for educational and portfolio purposes but has not undergone peer review.

> **Safety notice**
>
> The findings describe statistical associations in an academic dataset and must not be used to determine whether a real mushroom is safe to consume.

## Project overview

This case study examines how several unsupervised methods provide different
representations of the same high-dimensional categorical dataset. The analysis
uses the UCI Mushroom dataset as a controlled learning problem: class labels are
withheld from model fitting and used retrospectively to compare cluster
assignments.

**Research question:** How do different unsupervised learning techniques
represent, partition and explain high-dimensional categorical mushroom data?

The workflow combines categorical cleaning, One-Hot Encoding, UMAP, K-Means,
HDBSCAN, FP-Growth and Association Rule Mining. The executed notebook reports
clear local structure in the UMAP representation, weak agreement between
two-cluster K-Means on that representation and the reference labels, granular
density structure under HDBSCAN, and directly readable class-associated rules.

## Study at a glance

| Item | Verified study value |
|---|---:|
| Observations | 8,124 |
| Original predictors | 22 categorical variables |
| Predictors after constant-column removal | 21 |
| One-Hot encoded features | 115 |
| UMAP dimensions | 2 |
| K-Means clusters | 2 |
| K-Means ARI / NMI | 0.0636 / 0.0465 |
| Baseline HDBSCAN clusters / noise points | 87 / 31 |
| Association-rule thresholds | support ≥ 0.20; confidence ≥ 0.90 |

[Read the scientific report](paper/abstract.md){ .md-button .md-button--primary }

## Reproducibility

This website is the project's primary presentation layer. It provides the
research narrative, selected evidence and scientific interpretation without
reproducing the notebook cell by cell.

The advanced notebook is the **complete executable analysis and technical source
of truth** for preprocessing, parameter settings, computations and recorded
outputs. It is supplementary reproducible evidence for the synthesized report.
Where notebook prose and executed output disagree, the website uses the
executed output and records the discrepancy in the
[limitations](paper/limitations.md).

[Open the complete executable notebook](https://github.com/Bootcamp-IA-MAD-P7/unsupervised-ml-workshop/blob/feat/advanced-unsupervised-techniques/workshop-advanced-unsupervised.ipynb){ .md-button .md-button--primary }

[Repository](https://github.com/Bootcamp-IA-MAD-P7/unsupervised-ml-workshop)
· `workshop-advanced-unsupervised.ipynb`
