# Discussion

The experiments show why visual clarity and clustering quality must be assessed
separately. UMAP optimized a low-dimensional representation of local
neighbourhood structure; K-Means optimized distances to two centroids in that
representation. Compact islands can therefore look well separated while still
being divided by centroids in a way that agrees poorly with the two reference
classes. The recorded ARI 0.0116 and NMI 0.0079 are a useful negative result,
not a reason to discard the embedding.

UMAP's emphasis on local structure also helps explain the HDBSCAN result. Many
small, dense islands became candidate clusters, so the baseline model returned
92 clusters rather than the two labels present in the source dataset. Raising
`min_cluster_size` and `min_samples` forced progressively broader density
requirements: the cluster count fell from 77 to 5 over the sensitivity range,
while noise varied from 47 to 510 observations. The sequence was non-monotonic
because changing both parameters alters the density
hierarchy, stability selection and cluster assignments—not merely a fixed
threshold.

The mismatch is analytically plausible. A binary edible/poisonous label records
one human-defined outcome, whereas morphology can contain many natural local
structures. Retrospective labels make agreement measurable, but they do not
prove that a two-group partition is the only valid unsupervised organization.

Association rules supplied the clearest human-readable knowledge because they
expressed explicit combinations rather than coordinates or cluster identifiers.
Within the mined rules, `odor_n` appeared strongly on the edible side. The
poisonous side involved combinations of bruising, gill size and colour, ring
type, spore-print colour and population characteristics. This asymmetry matters:
the analysis supports statements about recurring combinations in this dataset,
not about a universal single-trait test.

Some encoded characteristics, including `stalk-shape_t`, `ring-number_o`,
`gill-spacing_c`, `gill-attachment_f`, `veil-color_w` and `stalk-root_b`,
occurred in rules for both classes. They may be frequent contextual items while
remaining weak standalone discriminators. One-Hot categories also inherit
dependencies from their source variables, so raw rule frequency must not be
confused with independent importance.

There is therefore no universal best method. UMAP is useful for visual
exploration, K-Means for a specified centroid partition, HDBSCAN for granular
density structure, and association rules for explicit co-occurrence knowledge.
Method selection should follow the analytical question.
