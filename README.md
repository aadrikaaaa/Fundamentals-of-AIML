# Fundamentals-of-AIML
# Campus Navigation and Route Planning Assistant

This project is a search-based AI system that helps students find routes between important campus locations such as the hostel, library, lab complex, canteen, and academic block.

The project is intentionally designed around the early modules of the **Fundamentals in AI and ML** syllabus. Instead of focusing on advanced machine learning, it applies:

- intelligent agent thinking
- problem formulation as a state-space search problem
- uninformed search
- informed search
- rule-based constraints for route selection

## Problem statement

Students often need to move quickly across campus while considering practical constraints such as distance, crowded paths, wheelchair accessibility, and shaded walkways. The aim of this project is to build a campus route planner that can recommend a suitable path using AI search techniques.

## Course relevance

This project directly aligns with the first 2.5 modules of the syllabus:

- Introduction to AI
- Intelligent agents and environments
- Problem solving agents
- Search strategies: uninformed and informed
- Knowledge representation through a graph-based campus model

## Features

- choose a start and destination
- run `BFS`, `DFS`, `UCS`, or `A*`
- restrict routes to accessible paths only
- avoid crowded paths
- prefer shaded paths
- inspect available campus locations

## Project structure

```text
campus_navigation_byop/
├── data/
│   └── campus_map.json
├── report/
│   └── Project_Report.md
├── src/
│   ├── campus_map.py
│   ├── planner.py
│   └── search.py
├── .gitignore
├── README.md
└── requirements.txt
```

## How it works

The campus is modeled as a graph:

- locations are nodes
- walkable connections are edges
- each edge stores distance, crowd level, accessibility, and shade information

The route planner then applies an AI search algorithm to find a path from the source to the destination.

### Algorithms used

- `BFS` for minimum-edge path discovery
- `DFS` for depth-first exploration
- `UCS` for cost-based route selection
- `A*` for heuristic-guided search using location coordinates

## How to run

Open a terminal in:

```bash
cd /Users/kinjalk/Downloads/BYOP/campus_navigation_byop
```

List the available locations:

```bash
python3 src/planner.py --start "Hostel A" --goal "Library" --list-locations
```

Find a basic shortest route with A*:

```bash
python3 src/planner.py --start "Hostel A" --goal "Lab Complex" --algorithm astar
```

Find a route that avoids crowded paths and prefers shade:

```bash
python3 src/planner.py \
  --start "Hostel B" \
  --goal "Auditorium" \
  --algorithm ucs \
  --accessible-only \
  --avoid-crowds \
  --prefer-shade
```

## Example use cases

- a fresher finding the best path from hostel to academic block
- a student choosing a less crowded route during lunch break
- a wheelchair user limiting the search to accessible paths
- comparing BFS and A* to study search efficiency

## Why this is a strong BYOP topic

- solves a real and relatable campus problem
- matches the syllabus already covered
- easy to demonstrate in a viva
- shows AI concepts clearly without needing advanced ML
- can be extended later with time-based rules, blocked roads, or a GUI

## Future improvements

- add time-of-day traffic patterns
- include temporary road closures
- add a simple web or mobile interface
- store multiple campuses
- visualize the route on a map

## Submission note

The detailed report for the project is available as Project Report.
