"""Export website figures from the executed credit-card notebooks."""

from __future__ import annotations

import base64
import io
import json
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "docs" / "figures"
SOURCES = {
    "credit_distributions.png": (
        ROOT / "workshop-clustering-creditcard.ipynb",
        19,
    ),
    "credit_pca_variance.png": (
        ROOT / "workshop-clustering-creditcard.ipynb",
        23,
    ),
    "credit_pca_projection.png": (
        ROOT / "workshop-clustering-creditcard.ipynb",
        24,
    ),
    "credit_k_selection.png": (
        ROOT / "workshop-clustering-creditcard.ipynb",
        27,
    ),
    "credit_dendrogram.png": (
        ROOT / "workshop-clustering-creditcard.ipynb",
        31,
    ),
    "credit_dbscan.png": (
        ROOT / "workshop-clustering-creditcard.ipynb",
        33,
    ),
    "credit_kmeans_clusters.png": (
        ROOT / "workshop-clustering-creditcard.ipynb",
        38,
    ),
    "credit_segment_profiles.png": (
        ROOT / "workshop-clustering-creditcard.ipynb",
        40,
    ),
    "credit_anomalies.png": (
        ROOT / "workshop-clustering-creditcard.ipynb",
        43,
    ),
    "credit_umap_hdbscan.png": (
        ROOT / "workshop-clustering-creditcard-advanced.ipynb",
        14,
    ),
}


def png_from_cell(notebook_path: Path, cell_number: int) -> bytes:
    notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
    cell = notebook["cells"][cell_number]
    for output in cell.get("outputs", []):
        payload = output.get("data", {}).get("image/png")
        if payload:
            if isinstance(payload, list):
                payload = "".join(payload)
            return base64.b64decode(payload)
    raise RuntimeError(
        f"{notebook_path.name} cell {cell_number} has no PNG output. "
        "Execute the notebook before exporting figures."
    )


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for filename, (notebook_path, cell_number) in SOURCES.items():
        payload = png_from_cell(notebook_path, cell_number)
        with Image.open(io.BytesIO(payload)) as image:
            image.save(OUTPUT_DIR / filename, dpi=(300, 300), optimize=True)
        print(f"exported {filename} ({notebook_path.name}, cell {cell_number})")


if __name__ == "__main__":
    main()
