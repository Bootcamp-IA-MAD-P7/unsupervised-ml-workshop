# Project Constitution

## Purpose

This repository follows a documentation-first and specification-driven workflow.

Every implementation, notebook, and document must align with the project specifications before code is written.

---

## Repository Principles

- Documentation comes before implementation.
- Understand the data before modelling.
- Every result must be reproducible.
- Every visualization must have an interpretation.
- Every technical decision should be documented.
- Business or academic conclusions are mandatory.
- Simplicity is preferred over unnecessary complexity.

---

## Notebook Principles

All notebooks must follow:

docs/notebook-spec.md

No notebook may deviate from this structure without justification.

---

## Data Science Principles

Before modelling:

- Explore the data.
- Assess data quality.
- Select an appropriate preprocessing strategy.
- Justify feature transformations.

Never fit a model before understanding the dataset.

---

## Machine Learning Principles

Algorithms must be selected because they fit the problem, not because they are popular.

Different datasets require different:

- preprocessing;
- distance metrics;
- validation strategies;
- interpretations.

No algorithm is considered universally superior.

---

## Documentation Principles

The following documents are part of the project:

- README.md
- project-plan.md
- methodology.md
- notebook-spec.md
- project-constitution.md
- decisions.md
- references.md
- daily/

Documentation must evolve together with the code.

---

## Git Principles

- Work on feature branches.
- Keep commits focused.
- Document important changes.
- Never commit datasets or virtual environments.
- Review changes before committing.

---

## AI Collaboration

AI tools may assist implementation.

They must not:

- redefine project scope;
- remove notebook sections;
- fabricate results;
- modify datasets;
- introduce dependencies without approval.

Before implementing code, AI assistants should review:

- notebook-spec.md
- methodology.md
- project-plan.md
- project-constitution.md

---

## Definition of Done

A task is complete only when:

- code works;
- notebook follows the specification;
- documentation is updated;
- results are interpreted;
- conclusions are written;
- changes are reproducible.

---

## Guiding Principle

Good Machine Learning is not only about obtaining metrics.

It is about understanding the data, choosing appropriate methods, documenting decisions, and producing reproducible analyses.