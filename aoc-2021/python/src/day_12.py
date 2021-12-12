import os
from typing import TextIO

import networkx as nx


def parse_input(input_file: TextIO) -> nx.Graph:
    return nx.Graph([line.strip().split("-") for line in input_file])


def get_routes(
    caves: nx.Graph, pos: str, visited: set[str], revisited_small: bool
) -> int:
    routes = 0
    print("getting routes from", pos)
    for next in caves.adj[pos].keys():
        if next == "end":
            print("reached end")
            routes += 1
        elif next == "start":
            continue
        elif next not in visited or revisited_small is False:
            next_visited = visited.union({next}) if next.islower() else visited
            routes += get_routes(
                caves, next, next_visited, revisited_small or next in visited
            )

    return routes


def count_paths(caves: nx.Graph) -> int:
    return get_routes(caves, "start", {"start"}, True)


def count_paths_2(caves: nx.Graph) -> int:
    return get_routes(caves, "start", {"start"}, False)


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    with open("../data/day_12.in") as input_file:
        caves = parse_input(input_file)

    print("part 1:", count_paths(caves))
    print("part 2:", count_paths_2(caves))
