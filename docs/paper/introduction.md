# Introduction

Unsupervised learning searches for structure without using a target variable to
fit the model. It can compress data, partition observations, identify
density-defined groups or discover attributes that repeatedly occur together.
Those are related but distinct analytical goals.

Categorical data make these tasks especially challenging. One-Hot Encoding
converts categories into binary indicators, but the resulting space is sparse
and high-dimensional. Distances can become difficult to interpret, correlated
indicators can encode the same underlying variable, and a visually convincing
two-dimensional projection can discard information needed by a clustering
algorithm.

No single algorithm answers every question in this setting:

- **Dimensionality reduction** creates a compact representation for exploration.
- **Clustering** partitions observations according to an optimization criterion.
- **Density analysis** finds locally dense regions and may label sparse points as noise.
- **Association-rule mining** expresses co-occurrence patterns as readable antecedent–consequent rules.

This Bootcamp case study therefore treats the algorithms as complementary
instruments. The class column is isolated before preprocessing and model fitting.
It returns only after clustering, as a retrospective reference for ARI and NMI,
or as a consequent during the rule-mining knowledge-discovery stage. This is a
practical academic analysis, not a scientific publication or a real-world
identification system.

## Research questions

1. Can UMAP reveal non-linear structure?
2. Does a visually clear embedding improve K-Means clustering?
3. What density structures does HDBSCAN reveal?
4. Which characteristics are most associated with edible and poisonous classes?
5. Which technique provides the most interpretable knowledge?
