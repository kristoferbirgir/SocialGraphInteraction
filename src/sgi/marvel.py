"""Load the course's frozen Marvel Wikipedia-links snapshot (week 1 release).

Source: https://sunelehmann.com/socialgraphs2026-web/data/
See ``scripts/download_marvel_week1.py`` for how the raw files got here, and
``data/raw/marvel/week1/MANIFEST.json`` for provenance (source URLs, retrieval
time, checksums).
"""

from __future__ import annotations

from pathlib import Path

import networkx as nx
import pandas as pd

from sgi.paths import MARVEL_RAW_DIR

NODES_FILENAME = "week1_nodes.tsv"
EDGES_FILENAME = "week1_edges.tsv"

# Published on the course data page for this frozen snapshot — treat these as
# checks against computed values, never as substitutes for computing them.
EXPECTED_NODE_COUNT = 303
EXPECTED_DIRECTED_EDGE_COUNT = 1784
EXPECTED_UNDIRECTED_EDGE_COUNT = 1434
EXPECTED_ISOLATE_COUNT = 17
EXPECTED_UNDIRECTED_COMPONENT_SIZES = tuple(sorted([277, 9, *([1] * 17)], reverse=True))


def load_nodes(nodes_path: Path) -> pd.DataFrame:
    """Read the node roster (node_id, name, wikidata_id, url, description)."""
    return pd.read_csv(nodes_path, sep="\t", comment="#", quoting=3)


def load_edges(edges_path: Path) -> pd.DataFrame:
    """Read the directed edge list (source, target)."""
    return pd.read_csv(edges_path, sep="\t", comment="#", names=["source", "target"])


def build_directed_graph(nodes: pd.DataFrame, edges: pd.DataFrame) -> nx.DiGraph:
    """Build the directed graph, adding every node before any edge.

    Adding nodes first is what keeps isolates in the graph — building straight
    from the edge list alone silently drops any node with no edges.
    """
    graph = nx.DiGraph()
    graph.add_nodes_from(nodes["node_id"])
    graph.add_edges_from(edges[["source", "target"]].itertuples(index=False, name=None))
    return graph


def to_undirected(graph: nx.DiGraph) -> nx.Graph:
    """Collapse directed edges into an undirected graph (A->B or B->A means A-B)."""
    return nx.Graph(graph.to_undirected(reciprocal=False))


def load_marvel_graph(raw_dir: Path = MARVEL_RAW_DIR) -> nx.DiGraph:
    """Load the week-1 Marvel snapshot as a directed graph with isolates preserved."""
    nodes = load_nodes(raw_dir / NODES_FILENAME)
    edges = load_edges(raw_dir / EDGES_FILENAME)
    return build_directed_graph(nodes, edges)


def snapshot_report(directed: nx.DiGraph) -> dict:
    """Compute the same summary statistics the course page reports, for comparison."""
    undirected = to_undirected(directed)
    component_sizes = sorted(
        (len(component) for component in nx.connected_components(undirected)),
        reverse=True,
    )
    return {
        "node_count": directed.number_of_nodes(),
        "directed_edge_count": directed.number_of_edges(),
        "undirected_edge_count": undirected.number_of_edges(),
        "isolate_count": len(list(nx.isolates(undirected))),
        "undirected_component_sizes": component_sizes,
    }
