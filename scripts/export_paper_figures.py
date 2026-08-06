"""Export verified figures from the executed advanced notebook.

The executed notebook is the source of truth for this report. Most figures are
therefore exported from its embedded outputs instead of rerunning stochastic
UMAP or generating more than three million association rules. The two HDBSCAN
sensitivity charts are rebuilt from the values printed by the executed cell.

Usage:
    python scripts/export_paper_figures.py
"""

from __future__ import annotations

import base64
import io
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "workshop-advanced-unsupervised.ipynb"
DATASET = ROOT / "data" / "mushrooms.csv"
OUTPUT_DIR = ROOT / "docs" / "figures"

PNG_CELLS = {
    "umap_projection.png": 8,
    "kmeans_vs_ground_truth.png": 11,
    "feature_frequency.png": 38,
    "dumbbell_features.png": 47,
    "feature_heatmap.png": 51,
    "association_network.png": 55,
}


def fail(message: str) -> None:
    raise RuntimeError(message)


def load_notebook() -> dict:
    if not NOTEBOOK.exists():
        fail(f"Required notebook not found: {NOTEBOOK}")
    if not DATASET.exists():
        fail(f"Required dataset not found: {DATASET}")
    return json.loads(NOTEBOOK.read_text(encoding="utf-8"))


def output_text(cell: dict) -> str:
    parts: list[str] = []
    for output in cell.get("outputs", []):
        parts.extend(output.get("text", []))
        plain = output.get("data", {}).get("text/plain")
        if plain:
            parts.extend(plain)
    return "".join(parts)


def validate_canonical_outputs(notebook: dict) -> None:
    checks = {
        4: ("Observations: 8124", "Encoded features: 115"),
        10: ("ARI : 0.0116", "NMI : 0.0079"),
        16: ("Clusters: 92", "Noise points: 24"),
        24: ("Association rules generated: 3462243",),
        35: (
            "Edible class rules analysed: 7,028",
            "Poisonous class rules analysed: 4,128",
        ),
        54: ("Network nodes: 17", "Network edges: 18"),
    }
    for cell_number, expected_values in checks.items():
        actual = output_text(notebook["cells"][cell_number])
        for expected in expected_values:
            if expected not in actual:
                fail(
                    f"Cell {cell_number} no longer contains the verified "
                    f"output {expected!r}. Review the notebook before exporting."
                )


def png_payload(cell: dict, cell_number: int) -> bytes:
    for output in cell.get("outputs", []):
        payload = output.get("data", {}).get("image/png")
        if payload:
            if isinstance(payload, list):
                payload = "".join(payload)
            return base64.b64decode(payload)
    fail(f"Cell {cell_number} has no embedded PNG output.")


def save_png_with_dpi(payload: bytes, destination: Path) -> None:
    try:
        from PIL import Image
    except ImportError as exc:
        fail(
            "Pillow is required to preserve PNG output with 300-DPI metadata. "
            "Install the project or figure-export dependencies first."
        )
    with Image.open(io.BytesIO(payload)) as image:
        image.save(destination, dpi=(300, 300), optimize=True)


def export_embedded_pngs(notebook: dict) -> None:
    for filename, cell_number in PNG_CELLS.items():
        payload = png_payload(notebook["cells"][cell_number], cell_number)
        save_png_with_dpi(payload, OUTPUT_DIR / filename)
        print(f"exported {filename} (notebook cell {cell_number})")


def parse_hdbscan_sensitivity(notebook: dict) -> tuple[list[int], list[int], list[int]]:
    text = output_text(notebook["cells"][18])
    matches = re.findall(
        r"min_cluster_size=\s*(\d+)\s+clusters=\s*(\d+)\s+noise=(\d+)",
        text,
    )
    if len(matches) != 5:
        fail("Could not parse the five verified HDBSCAN sensitivity results.")
    sizes, clusters, noise = zip(*(map(int, match) for match in matches))
    return list(sizes), list(clusters), list(noise)


def export_hdbscan_charts(notebook: dict) -> None:
    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        fail(
            "Matplotlib is required for the HDBSCAN sensitivity figures. "
            "Install the project dependencies first."
        )

    sizes, clusters, noise = parse_hdbscan_sensitivity(notebook)
    style = {
        "marker": "o",
        "linewidth": 2,
        "markersize": 6,
        "color": "#4051b5",
    }

    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    ax.plot(sizes, clusters, **style)
    ax.set(
        title="HDBSCAN cluster count sensitivity",
        xlabel="Minimum cluster size",
        ylabel="Clusters",
    )
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "hdbscan_cluster_count.png", dpi=300)
    plt.close(fig)
    print("exported hdbscan_cluster_count.png (parsed from notebook cell 18)")

    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    ax.plot(sizes, noise, **style)
    ax.set(
        title="HDBSCAN noise sensitivity",
        xlabel="Minimum cluster size",
        ylabel="Noise observations",
    )
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "hdbscan_noise.png", dpi=300)
    plt.close(fig)
    print("exported hdbscan_noise.png (parsed from notebook cell 18)")


def export_sankey(notebook: dict) -> None:
    try:
        import plotly.io as pio
    except ImportError:
        fail(
            "Plotly is required to export the embedded Sankey diagram. "
            "Install the project dependencies first."
        )

    cell_number = 59
    figure = None
    for output in notebook["cells"][cell_number].get("outputs", []):
        figure = output.get("data", {}).get("application/vnd.plotly.v1+json")
        if figure:
            break
    if not figure:
        fail(f"Cell {cell_number} has no embedded Plotly figure.")

    html = pio.to_html(figure, full_html=True, include_plotlyjs=True)
    (OUTPUT_DIR / "association_sankey.html").write_text(
        html,
        encoding="utf-8",
    )
    print(f"exported association_sankey.html (notebook cell {cell_number})")


def main() -> int:
    try:
        notebook = load_notebook()
        validate_canonical_outputs(notebook)
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        export_embedded_pngs(notebook)
        export_hdbscan_charts(notebook)
        export_sankey(notebook)
    except (RuntimeError, ValueError, json.JSONDecodeError) as exc:
        print(f"Figure export failed: {exc}", file=sys.stderr)
        return 1
    print(f"Verified figure export complete: {OUTPUT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
