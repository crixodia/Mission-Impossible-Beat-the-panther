import json
import sys

from pprint import pprint
from math import inf


def get_adjacency_dict(L):
    G = {}

    m = len(L)
    n = len(L[0])

    for i in range(m):
        for j in range(n):
            if L[i][j] != 0:
                continue

            G[(i, j)] = []
            if i + 1 < m:
                if L[i + 1][j] == 0:
                    G[(i, j)].append((i + 1, j))

            if j + 1 < n:
                if L[i][j + 1] == 0:
                    G[(i, j)].append((i, j + 1))

    return G


def find_shortest_path(G: dict, start: tuple, end: tuple):
    dist = {node: inf for node in G.keys()}
    prev = {node: None for node in G.keys()}

    dist[start] = 0

    unvisited = set(G.keys())

    while unvisited:
        current = min(unvisited, key=lambda node: dist[node])
        unvisited.remove(current)

        if dist[current] == inf:
            break

        for neighbour in G[current]:
            alt = dist[current] + 1
            if alt < dist[neighbour]:
                dist[neighbour] = alt
                prev[neighbour] = current

    path = []
    current = end
    while prev[current]:
        path.append(current)
        current = prev[current]
    path.append(current)

    return path[::-1]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        data = json.load(open(sys.argv[1]))

        L = data["l"]
        start = tuple(data["start"])
        end = tuple(data["end"])

        if len(sys.argv) > 2:
            if sys.argv[2] == "print":
                pprint(get_adjacency_dict(L))

        print(f"Shortest path: {find_shortest_path(get_adjacency_dict(L), start, end)}")
    else:
        print("Usage: python main.py <input.json> [print]")
        print("Example: python main.py samples/1.json print")
