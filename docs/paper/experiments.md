# Experiments

This page records the protocol. Outcomes are reported separately in
[Results](results.md).

## Experiment 1 — UMAP representation

**Objective.** Determine whether a non-linear two-dimensional representation
reveals local structure in the encoded categorical observations.

**Method.** Fit UMAP to the 115 One-Hot encoded features with two components and
random state 42.

**Evaluation.** Inspect the geometry without using class labels during fitting;
overlay labels only after embedding to support retrospective interpretation.

**Expected evidence.** Compact neighbourhoods or islands that are less apparent
in the original high-dimensional coordinates.

## Experiment 2 — K-Means on UMAP

**Objective.** Test whether the visually clear UMAP representation also supports
a two-cluster centroid partition aligned with the reference classes.

**Method.** Fit K-Means with two clusters, ten initializations and random state
42 to the UMAP coordinates.

**Evaluation.** Compare assignments with the withheld class labels using ARI and
NMI, and inspect clusters beside the label-coloured embedding.

**Reference comparison.** The comparison is limited to the executed UMAP result;
the original-space workshop is evaluated separately in its own notebook.

## Experiment 3 — UMAP + HDBSCAN

**Objective.** Discover local-density structures without fixing the number of
clusters and identify observations not assigned to a stable dense region.

**Method.** Fit the baseline HDBSCAN configuration to the UMAP embedding. Repeat
the fit over the recorded `min_cluster_size` values, with `min_samples` equal to
half of each size.

**Evaluation.** Record the number of non-noise clusters and the number of points
assigned label −1. Noise is interpreted as model uncertainty under a given
density configuration, not as a data error or biological anomaly.

## Experiment 4 — Association Rule Mining

**Objective.** Convert categorical co-occurrence into explicit, human-readable
class-predicting rules.

**Method.** Use FP-Growth to retain itemsets at or above 0.20 support, then
generate rules at or above 0.90 confidence. Filter consequents to exactly one
class item and summarize characteristic frequencies across these rules.

**Evaluation.** Review support, confidence and lift together. Support measures
prevalence, confidence measures conditional co-occurrence, and lift compares
the rule with the class base rate.

**Knowledge-discovery objective.** Identify recurring class-associated
combinations and distinguish class-specific features from frequent features
that occur in rules for both classes. No rule is treated as causal or as safety
advice.
