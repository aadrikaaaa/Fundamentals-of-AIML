# Campus Navigation and Route Planning Assistant

A search-based AI system that helps students find optimal routes between campus locations using intelligent algorithms.

**Status:** Production-ready  
**Language:** Python 3.8+  
**Algorithms:** BFS, DFS, UCS, A*  
**License:** Educational Use

---

## Overview

This project builds a practical AI agent that solves real-world routing problems on a college campus. Instead of blindly following the shortest path, it intelligently considers multiple constraints like accessibility, crowd levels, and shade availability.

The system models the campus as a directed graph and applies classical search algorithms to find paths that match student needs. It serves as both a useful tool and a demonstration of AI problem-solving techniques.

## Campus Locations

The system covers 12 major campus locations:

| Location | Type | Description |
|----------|------|-------------|
| **Hostels** | Residential | Hostel A, Hostel B |
| **Academic** | Education | Academic Block, Lab Complex |
| **Study** | Support | Library |
| **Food** | Amenity | Canteen |
| **Health** | Support | Medical Center |
| **Transport** | Entrance | Main Gate, Parking |
| **Office** | Administrative | Admin Block |
| **Events** | Recreation | Auditorium |
| **Sports** | Recreation | Sports Ground |

## System Architecture

### Components

1. **`campus_map.py`** - Graph data structure and heuristic functions
   - Loads campus graph from JSON
   - Stores location coordinates and edge metadata
   - Implements Euclidean distance heuristic for A*

2. **`search.py`** - Search algorithm implementations
   - BFS (Breadth-First Search)
   - DFS (Depth-First Search)
   - UCS (Uniform Cost Search)
   - A* (informed heuristic search)

3. **`planner.py`** - Command-line interface
   - User interaction layer
   - Argument parsing
   - Result formatting

### Data Model

The campus graph is represented in `campus_map.json`:

```json
{
  "nodes": {
    "Location Name": {"x": 0, "y": 1, "type": "category"}
  },
  "edges": [
    {
      "from": "Location A",
      "to": "Location B",
      "distance": 4,          // Physical distance
      "crowd": 3,             // Crowd level (1-5 scale)
      "accessible": true,     // Wheelchair accessible
      "shade": true           // Has shade coverage
    }
  ]
}
```

## Search Algorithms

### Uninformed Search

**Breadth-First Search (BFS)**
- Explores level-by-level from start
- Guarantees minimum-edge paths
- Best for: Finding paths with fewest stops
- Cost: No additional penalties applied

```bash
python3 src/planner.py --start "Hostel A" --goal "Library" --algorithm bfs
```

**Depth-First Search (DFS)**
- Explores deeply before backtracking
- Good for exploring unfamiliar campuses
- Best for: Complete path discovery
- Useful for: Understanding campus connectivity

```bash
python3 src/planner.py --start "Hostel A" --goal "Lab Complex" --algorithm dfs
```

### Informed Search

**Uniform Cost Search (UCS)**
- Considers edge costs (distance + constraints)
- Balances multiple factors
- Best for: Cost-aware routing with constraints
- Respects: `--avoid-crowds` and `--prefer-shade` flags

Cost calculation:
```
cost = distance + (avoid_crowds ? crowd_level * 0.8 : 0) + (prefer_shade ? 1.5 : 0)
```

```bash
python3 src/planner.py \
  --start "Hostel B" \
  --goal "Auditorium" \
  --algorithm ucs \
  --avoid-crowds \
  --prefer-shade
```

**A* Search** (Recommended)
- Uses Euclidean distance heuristic
- Optimal and efficient
- Best for: Fast, intelligent route planning
- Respects: `--avoid-crowds` and `--prefer-shade` flags

```bash
python3 src/planner.py \
  --start "Hostel A" \
  --goal "Lab Complex" \
  --algorithm astar
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

```bash
# Clone or download the project
cd /Users/kinjalk/Downloads/BYOP/campus_navigation_byop

# Install dependencies (if any)
pip install -r requirements.txt
```

## Usage

### Basic Commands

**1. List all available locations:**
```bash
python3 src/planner.py --start "Hostel A" --goal "Library" --list-locations
```

Output:
```
Available locations:
- Academic Block
- Admin Block
- Auditorium
- Canteen
- Hostel A
- Hostel B
- Lab Complex
- Library
- Main Gate
- Medical Center
- Parking
- Sports Ground
```

> Note: The `--start` and `--goal` arguments are required by the parser but ignored when using `--list-locations`.

### Route Planning

**2. Quick route with default A* algorithm:**
```bash
python3 src/planner.py --start "Hostel A" --goal "Library"
```

**3. Find accessible-only paths (wheelchair-friendly):**
```bash
python3 src/planner.py \
  --start "Hostel A" \
  --goal "Lab Complex" \
  --accessible-only
```

**4. Avoid crowded areas:**
```bash
python3 src/planner.py \
  --start "Hostel B" \
  --goal "Canteen" \
  --algorithm ucs \
  --avoid-crowds
```

**5. Prefer shaded paths:**
```bash
python3 src/planner.py \
  --start "Medical Center" \
  --goal "Sports Ground" \
  --algorithm astar \
  --prefer-shade
```

**6. Combine multiple constraints:**
```bash
python3 src/planner.py \
  --start "Hostel B" \
  --goal "Auditorium" \
  --algorithm ucs \
  --accessible-only \
  --avoid-crowds \
  --prefer-shade
```

**7. Use a custom map file:**
```bash
python3 src/planner.py \
  --start "Hostel A" \
  --goal "Library" \
  --map-file /path/to/custom_map.json
```

## Output Explanation

When a route is found, you'll see:

```
Algorithm used        : A*
Path                  : Hostel A -> Canteen -> Library
Total distance        : 7.0
Search cost           : 7.0
Expanded nodes        : 5
Accessible only       : False
Avoid crowds          : False
Prefer shade          : False
```

### Metrics

| Metric | Meaning |
|--------|---------|
| **Path** | Sequence of locations from start to goal |
| **Total distance** | Sum of edge distances in the path |
| **Search cost** | Cost used by algorithm (includes crowd/shade penalties) |
| **Expanded nodes** | Number of nodes explored during search |

## Educational Value

This project demonstrates:

- **Problem Formulation**: Representing campus as state-space graph
- **Uninformed Search**: BFS and DFS guarantee completeness
- **Informed Search**: A* combines optimality with efficiency
- **Constraint Handling**: Real-world rules (accessibility, preferences)
- **Graph Algorithms**: Adjacency lists, heuristics, path reconstruction
- **Agent Design**: Goal-driven problem solving

## Command Reference

```bash
python3 src/planner.py [options]

Required Arguments:
  --start LOCATION              Starting location (required by parser)
  --goal LOCATION               Destination location (required by parser)

Optional Arguments:
  --algorithm {bfs|dfs|ucs|astar}  Search algorithm (default: astar)
  --accessible-only             Only use wheelchair-accessible paths
  --avoid-crowds                Penalize high-crowd routes
  --prefer-shade                Prefer shaded walkways
  --map-file PATH               Path to campus_map.json (auto-detected by default)
  --list-locations              Show all available locations and exit

Examples:
  # Show available locations
  python3 src/planner.py --start "X" --goal "X" --list-locations

  # Basic routing
  python3 src/planner.py --start "Hostel A" --goal "Library"

  # Accessible routing
  python3 src/planner.py --start "Hostel A" --goal "Lab Complex" --accessible-only

  # With constraints
  python3 src/planner.py --start "Hostel B" --goal "Auditorium" --algorithm ucs --avoid-crowds --prefer-shade
```

## Algorithm Comparison

| Algorithm | Time | Space | Optimal | Use Case |
|-----------|------|-------|---------|----------|
| **BFS** | O(V+E) | O(V) | ✓ (edges) | Fewest stops |
| **DFS** | O(V+E) | O(V) | ✗ | Exploration |
| **UCS** | O(E log V) | O(V) | ✓ | Cost-aware |
| **A*** | O(E log V) | O(V) | ✓ | Recommended |

## Use Cases

### Scenario 1: Fresher's First Day
Find the fastest route from hostel to class:
```bash
python3 src/planner.py --start "Hostel A" --goal "Academic Block" --algorithm astar
```

### Scenario 2: Avoiding Crowds
Lunch time routing that avoids busy paths:
```bash
python3 src/planner.py \
  --start "Hostel B" \
  --goal "Canteen" \
  --algorithm ucs \
  --avoid-crowds
```

### Scenario 3: Wheelchair Accessibility
Creating an inclusive route:
```bash
python3 src/planner.py \
  --start "Main Gate" \
  --goal "Library" \
  --accessible-only
```

### Scenario 4: Comfort Priority
A shaded route during hot weather:
```bash
python3 src/planner.py \
  --start "Hostel A" \
  --goal "Sports Ground" \
  --algorithm astar \
  --prefer-shade
```

### Scenario 5: Algorithm Comparison
Study how different algorithms solve the same problem:
```bash
# Compare all algorithms for a route
for algo in bfs dfs ucs astar; do
  echo "=== $algo ==="
  python3 src/planner.py --start "Hostel A" --goal "Lab Complex" --algorithm $algo
done
```

## Project Structure

```
campus_navigation_byop/
├── data/
│   └── campus_map.json          # Graph data: locations and edges
├── report/
│   └── Project_Report.md        # Detailed project documentation
├── src/
│   ├── campus_map.py            # Graph representation
│   ├── planner.py               # Main CLI application
│   ├── search.py                # Algorithm implementations
│   └── __pycache__/
├── .gitignore
├── README.md                    # This file
└── requirements.txt             # Dependencies
```

## File Descriptions

### `campus_map.json`
- Defines all 12 campus locations with coordinates
- Lists all bidirectional paths between locations
- Encodes path properties: distance, crowd level, accessibility, shade

### `campus_map.py`
- `CampusMap` class: loads and manages graph
- `Edge` dataclass: represents path properties
- `heuristic()`: Euclidean distance for A*
- `neighbors()`: returns adjacent locations
- `locations()`: lists all available spots

### `search.py`
- `bfs()`: Breadth-first search implementation
- `dfs()`: Depth-first search implementation
- `uniform_cost_search()`: Cost-optimized search
- `a_star()`: A* with Euclidean heuristic
- `RouteResult` dataclass: encapsulates search results

### `planner.py`
- Argument parsing with argparse
- Graph loading and validation
- Algorithm selection and execution
- Results formatting and display

## 🔗 Related Resources

- **Full Project Report**: [Project_Report.md](report/Project_Report.md)
- **Course Alignment**: Covers AI/ML modules 1-2.5 (Fundamentals)
- **Algorithms Reference**: See search.py for annotated implementations

## Future Enhancements

- ✨ Time-of-day traffic patterns
- ✨ Real-time crowd data integration
- ✨ Temporary road closure handling
- ✨ Web interface for visualization
- ✨ Mobile app support
- ✨ Multi-campus support
- ✨ Route caching and analytics

## Notes

- The `--start` and `--goal` parameters are required arguments for the argument parser but are ignored when `--list-locations` is used
- All paths are bidirectional (going from A to B is same as B to A)
- Accessibility, crowd, and shade properties are pre-computed static attributes
- The heuristic function uses Euclidean distance based on stored coordinates
- All distances are in consistent units (campus grid units)

## Author Notes

This project was built as a strong BYOP (Build Your Own Project) submission because it:

✅ Solves a real, relatable problem  
✅ Directly aligns with early course syllabus  
✅ Demonstrates core AI concepts without advanced ML  
✅ Works well in viva demonstrations  
✅ Has clear output and easy validation  
✅ Can be extended with interesting features  

## License

Educational use only. For more details, see project documentation.
