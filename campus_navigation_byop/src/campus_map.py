from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Edge:
    destination: str
    distance: float
    crowd: int
    accessible: bool
    shade: bool


class CampusMap:
    def __init__(self, nodes: dict[str, dict], adjacency: dict[str, list[Edge]]) -> None:
        self.nodes = nodes
        self.adjacency = adjacency

    @classmethod
    def load(cls, map_path: Path) -> "CampusMap":
        payload = json.loads(map_path.read_text(encoding="utf-8"))
        adjacency: dict[str, list[Edge]] = {name: [] for name in payload["nodes"]}
        for edge in payload["edges"]:
            forward = Edge(
                destination=edge["to"],
                distance=edge["distance"],
                crowd=edge["crowd"],
                accessible=edge["accessible"],
                shade=edge["shade"],
            )
            reverse = Edge(
                destination=edge["from"],
                distance=edge["distance"],
                crowd=edge["crowd"],
                accessible=edge["accessible"],
                shade=edge["shade"],
            )
            adjacency[edge["from"]].append(forward)
            adjacency[edge["to"]].append(reverse)
        return cls(nodes=payload["nodes"], adjacency=adjacency)

    def has_location(self, name: str) -> bool:
        return name in self.nodes

    def neighbors(self, name: str) -> list[Edge]:
        return self.adjacency.get(name, [])

    def heuristic(self, source: str, target: str) -> float:
        node_a = self.nodes[source]
        node_b = self.nodes[target]
        return math.dist((node_a["x"], node_a["y"]), (node_b["x"], node_b["y"]))

    def locations(self) -> list[str]:
        return sorted(self.nodes.keys())
