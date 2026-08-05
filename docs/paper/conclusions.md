# Conclusions

This study tested explicit hypotheses about representation, partitioning,
density and interpretability rather than merely applying a sequence of
algorithms. UMAP improved visual exploration of the encoded categorical data,
but visual clarity and clustering agreement were not equivalent. K-Means on the
two-dimensional embedding showed weak retrospective agreement with the binary
labels, and that negative result was retained as evidence.

HDBSCAN exposed granular, parameter-sensitive density structures rather than a
fixed two-class partition. Association Rule Mining produced the clearest
human-readable knowledge: the absence-of-odor indicator `odor_n` was strongly
represented in edible rules, while poisonous patterns involved combinations of
bruising, gill, ring, spore-print and population characteristics. These are
dataset associations, not causal findings or identification guidance.

The central conclusion is methodological. Dimensionality reduction, centroid
clustering, density analysis and rule mining answer different questions.
Selecting a method therefore requires matching its objective to the analytical
purpose, including preserving and interpreting unexpected or negative results.

## What I learned

I learned to separate an attractive visualization from quantitative clustering
evidence, to treat parameter sensitivity as a result rather than a nuisance,
and to use association rules as a bridge from high-dimensional encoded data to
auditable statements. Most importantly, I learned that a responsible portfolio
case study should make its uncertainty, academic status and safety boundaries
as visible as its successful findings.
