# Abstract

**Background.** One-Hot Encoding of categorical data produces a sparse,
high-dimensional representation in which algorithms emphasize different forms
of structure. This report is an academic case study, not a peer-reviewed
publication.

**Objective.** The study asks: *How do different unsupervised learning
techniques represent, partition and explain high-dimensional categorical
mushroom data?*

**Methods.** The executed notebook analyzes 8,124 observations from the UCI
Mushroom dataset. After missing-value treatment, mode imputation, removal of
constant `veil-type` and class separation, 21 categorical predictors were
One-Hot encoded into 115 features. UMAP produced a two-dimensional
representation. K-Means and HDBSCAN examined centroid and local-density
structure.
FP-Growth and Association Rule Mining identified frequent categorical
combinations. Class labels were not used to fit the unsupervised models; they
were used retrospectively for Adjusted Rand Index (ARI) and Normalized Mutual
Information (NMI) validation.

**Results.** K-Means on UMAP achieved ARI 0.0116 and NMI 0.0079, showing that
visual separation did not translate into close reference-label agreement.
Baseline HDBSCAN returned 92 clusters and 24 noise observations; sensitivity
settings produced 5–77 clusters. Association mining generated 3,462,243 rules;
7,028 predicted edible and 4,128 predicted poisonous. `odor_n` recurred strongly
in edible rules, whereas poisonous patterns combined categorical traits.

**Conclusion.** No method was universally best. UMAP supported exploration,
HDBSCAN exposed granular density structure, and association rules offered the
most human-readable knowledge. These dataset associations are not mushroom
safety guidance.
