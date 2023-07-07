# Día 19: Buscar Elementos Duplicados en un Arreglo

Escribe un programa que encuentre y muestre duplicados en un arreglo de enteros.

- [Día 19: Buscar Elementos Duplicados en un Arreglo](#día-19-buscar-elementos-duplicados-en-un-arreglo)
  - [Contexto](#contexto)
  - [Solución](#solución)
  - [Resultados](#resultados)

## Contexto

Aprovecharemos Counter de la librería collections para contar los elementos de un arreglo y así encontrar los duplicados. Luego recorremos el diccionario generado y mostramos los elementos que tienen un valor mayor a 1.

## Solución

```python
from collections import Counter
from random import randint

def get_duplicated(elements:list) -> list:
    C = Counter(elements)
    return [k for k, v in C.items() if v > 1]
```

## Resultados

```bash
python .\main.py
Original:  [8, 7, 4, 3, 3, 9, 7, 10, 3, 7, 2, 6, 1, 1, 1, 2, 8, 3, 9, 5]
Duplicated:  [8, 7, 3, 9, 2, 1]
```
