# Technical Decisions

This document records the most relevant technical decisions taken during the project.

Each decision includes its context, rationale and expected impact.

---

# D-001 · Git Workflow

## Context

The project will be developed over several sessions.

## Decision

Use feature branches to isolate new work.

## Rationale

A feature branch workflow keeps the main branch stable, improves traceability and produces a cleaner Git history.

## Impact

- Cleaner commits.
- Easier code review.
- Better project organization.

---

# D-002 · Continuous Documentation

## Context

The project combines Machine Learning implementation with technical documentation.

## Decision

Maintain documentation throughout the development process instead of writing it only at the end.

## Rationale

Continuous documentation improves reproducibility, facilitates project review and supports the final presentation.

## Impact

- Better project traceability.
- Easier maintenance.
- Reduced documentation effort at the end.

---

# D-003 · Data Science Workflow

## Context

Two different datasets will be analysed using the same general methodology.

## Decision

Adopt a structured Data Science workflow for both notebooks.

## Workflow

Business Understanding

↓

Data Understanding

↓

Exploratory Data Analysis

↓

Data Cleaning

↓

Feature Engineering

↓

Dimensionality Reduction

↓

Clustering

↓

Validation

↓

Business Interpretation

↓

Conclusions

## Rationale

Using a consistent workflow improves reproducibility and ensures that both analyses follow the same methodological criteria.

## Impact

- Consistent analysis.
- Easier comparison between datasets.
- Better documentation.

---

# Future Decisions

This document will be updated as new technical decisions are made during the project.

Examples:

- D-004 · Missing value strategy
- D-005 · Feature encoding
- D-006 · PCA configuration
- D-007 · Clustering algorithm selection
- D-008 · Validation metrics
- D-009 · Isolation Forest configuration

## 2026-08-05 — Defer optional extensions

**Context:** The notebook proposes UMAP, HDBSCAN and association rules as optional extensions.

**Decision:** Keep these techniques documented but do not implement them during the mandatory workshop workflow.

**Rationale:** The required learning objectives are already covered, and these extensions introduce additional dependencies and analytical scope.

**Impact:** Optional techniques may be implemented later in dedicated feature branches after the mandatory notebooks are validated.