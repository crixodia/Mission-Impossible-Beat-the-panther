# Día 21: Matriz Transpuesta

Escribe un programa que calcule la matriz transpuesta.

- [Día 21: Matriz Transpuesta](#día-21-matriz-transpuesta)
  - [Contexto](#contexto)
  - [Solución](#solución)
  - [Resultados](#resultados)

## Contexto

Para calcular la matriz transpuesta simplemente hacemos que la filas de la matriz se vuelvan columnas. Esto es particularmente sencillo en Pyhton gracias a la función `zip()`.

## Solución

```python
def transpose(mat: list) -> list:
    return [list(i) for i in zip(*mat)]
```

Puedes encontrar el código completo en [main.py](main.py).

## Resultados


```bash
python .\main.py
Original matrix: 
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

Transposed matrix: 
[[1, 4, 7],
 [2, 5, 8],
 [3, 6, 9]]
```