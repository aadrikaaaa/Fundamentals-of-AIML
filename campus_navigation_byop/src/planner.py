from __future__ import annotations

import argparse
from pathlib import Path

from campus_map import CampusMap
from search import a_star, bfs, dfs, uniform_cost_search


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Campus navigation assistant using AI search algorithms.")
    parser.add_argument("--start", required=True, help="Starting location")
    parser.add_argument("--goal", required=True, help="Destination location")
    parser.add_argument(
        "--algorithm",
        choices=["bfs", "dfs", "ucs", "astar"],
        default="astar",
        help="Search algorithm to use",
    )
    parser.add_argument("--accessible-only", action="store_true", help="Use wheelchair-friendly paths only")
    parser.add_argument("--avoid-crowds", action="store_true", help="Penalize crowded routes")
    parser.add_argument("--prefer-shade", action="store_true", help="Prefer shaded walkways")
    parser.add_argument(
        "--map-file",
        default=str(Path(__file__).resolve().parents[1] / "data" / "campus_map.json"),
        help="Path to the campus map JSON file",
    )
    parser.add_argument("--list-locations", action="store_true", help="Print available locations and exit")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    campus_map = CampusMap.load(Path(args.map_file))

    if args.list_locations:
        print("Available locations:")
        for location in campus_map.locations():
            print(f"- {location}")
        return

    if not campus_map.has_location(args.start) or not campus_map.has_location(args.goal):
        print("Invalid location name.")
        print("Use --list-locations to see valid nodes in the campus map.")
        return

    if args.algorithm == "bfs":
        result = bfs(campus_map, args.start, args.goal, args.accessible_only)
    elif args.algorithm == "dfs":
        result = dfs(campus_map, args.start, args.goal, args.accessible_only)
    elif args.algorithm == "ucs":
        result = uniform_cost_search(
            campus_map,
            args.start,
            args.goal,
            args.accessible_only,
            args.avoid_crowds,
            args.prefer_shade,
        )
    else:
        result = a_star(
            campus_map,
            args.start,
            args.goal,
            args.accessible_only,
            args.avoid_crowds,
            args.prefer_shade,
        )

    if result is None:
        print("No valid route found with the selected constraints.")
        return

    print(f"Algorithm used        : {result.algorithm}")
    print(f"Path                  : {' -> '.join(result.path)}")
    print(f"Total distance        : {result.total_distance:.1f}")
    print(f"Search cost           : {result.total_cost:.1f}")
    print(f"Expanded nodes        : {result.expanded_nodes}")
    print(f"Accessible only       : {args.accessible_only}")
    print(f"Avoid crowds          : {args.avoid_crowds}")
    print(f"Prefer shade          : {args.prefer_shade}")


if __name__ == "__main__":
    main()
