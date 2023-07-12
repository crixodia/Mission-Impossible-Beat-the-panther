# Día 23: Red de Caminos

- [Día 23: Red de Caminos](#día-23-red-de-caminos)
  - [Contexto](#contexto)
  - [Solución](#solución)
  - [Resultados](#resultados)

En una antigua ciudad, existen diversas atracciones turísticas que están conectadas por una red de caminos. Cada camino tiene una longitud asociada que representa la distancia entre dos atracciones. Como entusiasta de la programación, te han desafiado a escribir un programa que encuentra el camino más corto entre dos atracciones en base a la red de caminos existentes.

## Contexto

Este reto puede resolverse gracias a la teoría de grafos. Para ello usaremos el algoritmo de cominos mínimos de Dijkstra.

## Solución

```python
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
```

Puedes encontrar el código completo en [main.py](main.py).

## Resultados

Para la red de caminos:

```python
red_caminos = {
    "A": ["B", "C", "D"],
    "B": ["C", "D"],
    "C": ["D", "E"],
    "D": ["E"],
    "E": [],
}

```

Se obtiene el siguiente resultado:

```bash
['A', 'D', 'E']
```
