from __future__ import annotations

import heapq
from collections import deque
from dataclasses import dataclass

from campus_map import CampusMap, Edge


@dataclass
class RouteResult:
    algorithm: str
    path: list[str]
    total_distance: float
    expanded_nodes: int
    total_cost: float


def is_edge_allowed(edge: Edge, accessible_only: bool) -> bool:
    if accessible_only and not edge.accessible:
        return False
    return True


def edge_cost(edge: Edge, avoid_crowds: bool, prefer_shade: bool) -> float:
    cost = edge.distance
    if avoid_crowds:
        cost += edge.crowd * 0.8
    if prefer_shade and not edge.shade:
        cost += 1.5
    return cost


def reconstruct(parents: dict[str, str | None], goal: str) -> list[str]:
    path = []
    current: str | None = goal
    while current is not None:
        path.append(current)
        current = parents[current]
    return list(reversed(path))


def compute_distance(campus_map: CampusMap, path: list[str]) -> float:
    total = 0.0
    for left, right in zip(path, path[1:]):
        for edge in campus_map.neighbors(left):
            if edge.destination == right:
                total += edge.distance
                break
    return total


def bfs(campus_map: CampusMap, start: str, goal: str, accessible_only: bool) -> RouteResult | None:
    frontier = deque([start])
    parents = {start: None}
    expanded = 0

    while frontier:
        current = frontier.popleft()
        expanded += 1
        if current == goal:
            path = reconstruct(parents, goal)
            distance = compute_distance(campus_map, path)
            return RouteResult("BFS", path, distance, expanded, distance)
        for edge in campus_map.neighbors(current):
            if not is_edge_allowed(edge, accessible_only):
                continue
            if edge.destination not in parents:
                parents[edge.destination] = current
                frontier.append(edge.destination)
    return None


def dfs(campus_map: CampusMap, start: str, goal: str, accessible_only: bool) -> RouteResult | None:
    stack = [start]
    parents = {start: None}
    expanded = 0

    while stack:
        current = stack.pop()
        expanded += 1
        if current == goal:
            path = reconstruct(parents, goal)
            distance = compute_distance(campus_map, path)
            return RouteResult("DFS", path, distance, expanded, distance)
        for edge in reversed(campus_map.neighbors(current)):
            if not is_edge_allowed(edge, accessible_only):
                continue
            if edge.destination not in parents:
                parents[edge.destination] = current
                stack.append(edge.destination)
    return None


def uniform_cost_search(
    campus_map: CampusMap,
    start: str,
    goal: str,
    accessible_only: bool,
    avoid_crowds: bool,
    prefer_shade: bool,
) -> RouteResult | None:
    heap: list[tuple[float, str]] = [(0.0, start)]
    parents = {start: None}
    best_cost = {start: 0.0}
    expanded = 0

    while heap:
        current_cost, current = heapq.heappop(heap)
        if current_cost > best_cost[current]:
            continue
        expanded += 1
        if current == goal:
            path = reconstruct(parents, goal)
            return RouteResult("UCS", path, compute_distance(campus_map, path), expanded, current_cost)
        for edge in campus_map.neighbors(current):
            if not is_edge_allowed(edge, accessible_only):
                continue
            new_cost = current_cost + edge_cost(edge, avoid_crowds, prefer_shade)
            if new_cost < best_cost.get(edge.destination, float("inf")):
                best_cost[edge.destination] = new_cost
                parents[edge.destination] = current
                heapq.heappush(heap, (new_cost, edge.destination))
    return None


def a_star(
    campus_map: CampusMap,
    start: str,
    goal: str,
    accessible_only: bool,
    avoid_crowds: bool,
    prefer_shade: bool,
) -> RouteResult | None:
    heap: list[tuple[float, float, str]] = [(campus_map.heuristic(start, goal), 0.0, start)]
    parents = {start: None}
    best_cost = {start: 0.0}
    expanded = 0

    while heap:
        _, current_cost, current = heapq.heappop(heap)
        if current_cost > best_cost[current]:
            continue
        expanded += 1
        if current == goal:
            path = reconstruct(parents, goal)
            return RouteResult("A*", path, compute_distance(campus_map, path), expanded, current_cost)
        for edge in campus_map.neighbors(current):
            if not is_edge_allowed(edge, accessible_only):
                continue
            new_cost = current_cost + edge_cost(edge, avoid_crowds, prefer_shade)
            if new_cost < best_cost.get(edge.destination, float("inf")):
                best_cost[edge.destination] = new_cost
                parents[edge.destination] = current
                priority = new_cost + campus_map.heuristic(edge.destination, goal)
                heapq.heappush(heap, (priority, new_cost, edge.destination))
    return None
