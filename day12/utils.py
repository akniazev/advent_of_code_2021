from collections import defaultdict


def is_small_cave(direction: str) -> bool:
    return direction.islower() and direction not in {"start", "end"}


def create_graph(lines: list[str]):
    graph = defaultdict(set)
    for line in lines:
        graph[line[0]].add(line[1])
        graph[line[1]].add(line[0])
    return graph


def visit_direction(direction: str,
                    current_path: tuple,
                    graph: dict[str, set[str]],
                    traveled_paths: set[tuple],
                    visited_small_caves: set[str],
                    should_visit_twice: bool = False,
                    visiting_twice: bool = False):
    if direction == "end":
        traveled_paths.add(current_path + ('end',))
        return
    if direction == "start":
        return
    if is_small_cave(direction):
        if direction in visited_small_caves:
            if not should_visit_twice or visiting_twice:
                return
            else:
                visiting_twice = True
        else:
            visited_small_caves = visited_small_caves.copy()
            visited_small_caves.add(direction)

    next_path = current_path + (direction,)
    traveled_paths.add(next_path)
    adjacent = graph[direction]

    for next_direction in adjacent:
        future_path = next_path + (next_direction,)
        if future_path not in traveled_paths:
            visit_direction(next_direction, next_path, graph, traveled_paths, visited_small_caves,
                            should_visit_twice=should_visit_twice,
                            visiting_twice=visiting_twice)


def find_paths(lines: list[str], visit_twice: bool = False) -> list[tuple]:
    graph = create_graph(lines)
    start_set = graph['start']
    traveled_paths = set()
    for direction in start_set:
        visited_small_caves = {direction} if is_small_cave(direction) else set()
        current_path = ('start', direction)
        traveled_paths.add(current_path)
        adjacent = graph[direction]
        for next_direction in adjacent:
            visit_direction(next_direction, current_path, graph, traveled_paths, visited_small_caves, visit_twice)

    return list(filter(lambda path: path[-1] == "end", traveled_paths))
