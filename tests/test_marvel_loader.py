"""Tests for the Marvel graph loader, using small local fixtures (no network)."""

from __future__ import annotations

from pathlib import Path

from sgi.marvel import build_directed_graph, load_edges, load_nodes, snapshot_report, to_undirected

FIXTURES_DIR = Path(__file__).parent / "fixtures"


def _load_fixture_graph():
    nodes = load_nodes(FIXTURES_DIR / "mini_nodes.tsv")
    edges = load_edges(FIXTURES_DIR / "mini_edges.tsv")
    return build_directed_graph(nodes, edges)


def test_load_nodes_reads_full_roster():
    nodes = load_nodes(FIXTURES_DIR / "mini_nodes.tsv")
    assert list(nodes["node_id"]) == ["Alpha", "Bravo", "Charlie", "Delta"]


def test_load_edges_reads_directed_pairs():
    edges = load_edges(FIXTURES_DIR / "mini_edges.tsv")
    assert list(edges.itertuples(index=False, name=None)) == [
        ("Alpha", "Bravo"),
        ("Bravo", "Alpha"),
        ("Alpha", "Charlie"),
    ]


def test_isolate_survives_because_nodes_are_added_first():
    graph = _load_fixture_graph()
    assert graph.number_of_nodes() == 4
    assert graph.number_of_edges() == 3
    assert "Delta" in graph.nodes
    assert graph.degree("Delta") == 0


def test_reciprocal_directed_edges_collapse_to_one_undirected_edge():
    graph = _load_fixture_graph()
    undirected = to_undirected(graph)

    # Alpha<->Bravo (reciprocal) and Alpha->Charlie (one-way) both become
    # single undirected edges: 3 directed edges -> 2 undirected edges.
    assert undirected.number_of_edges() == 2
    assert undirected.has_edge("Alpha", "Bravo")
    assert undirected.has_edge("Alpha", "Charlie")
    assert not undirected.has_edge("Bravo", "Charlie")


def test_isolate_has_no_edges_in_undirected_graph_either():
    graph = _load_fixture_graph()
    undirected = to_undirected(graph)
    assert undirected.degree("Delta") == 0


def test_snapshot_report_shape():
    graph = _load_fixture_graph()
    report = snapshot_report(graph)

    assert report["node_count"] == 4
    assert report["directed_edge_count"] == 3
    assert report["undirected_edge_count"] == 2
    assert report["isolate_count"] == 1
    assert report["undirected_component_sizes"] == [3, 1]
