# Limitations

> **Safety notice**
>
> This report describes statistical associations in a curated academic dataset.
> It must not be used to identify mushrooms or determine whether a real mushroom
> is safe to consume.

- This is a Machine Learning Bootcamp exercise structured as a scientific
  report; it is not peer reviewed and does not claim publication-level
  validation.
- The Mushroom dataset is curated and categorical. Its sampling, coding and
  historical scope constrain the conclusions.
- UMAP includes stochastic optimization. A random seed improves
  reproducibility but does not remove version- and environment-dependent
  behavior.
- A two-dimensional embedding necessarily loses information from the 115
  encoded features.
- HDBSCAN is sensitive to density parameters. The observed cluster and noise
  counts apply only to the recorded settings and embedding.
- Labels were used retrospectively for ARI and NMI. This external validation
  does not make the clustering procedure supervised, but it frames evaluation
  around a pre-existing binary partition.
- Association-rule output is highly redundant: 3,462,243 rules were generated
  at the recorded thresholds.
- Confidence measures conditional co-occurrence; it does not imply causality.
  Likewise, rule frequency and lift do not establish causal or biological
  importance.
- One-Hot encoded categories can be mutually exclusive or strongly correlated,
  violating a naive interpretation of items as independent evidence.
- Findings have not been tested on another dataset, so no generalization beyond
  this analysis is claimed.
- The data and analysis provide no real-world mushroom-safety guidance.
