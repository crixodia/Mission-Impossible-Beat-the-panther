from math import inf


def find_shortest_path(G: dict, start: str, end: str):
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

red_caminos = {
    "A": ["B", "C", "D"],
    "B": ["C", "D"],
    "C": ["D", "E"],
    "D": ["E"],
    "E": [],
}

print(find_shortest_path(red_caminos, "A", "E"))