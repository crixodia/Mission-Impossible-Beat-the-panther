# Día 20:  Número Faltante

Escribe un programa que encuentre el número faltante en una secuencia de número enteros consecutivos.

- [Día 20:  Número Faltante](#día-20--número-faltante)
  - [Solución](#solución)
  - [Resultados](#resultados)

## Solución

Recorremos la lista de números y cuando encontramos un número que no es igual al número anterior más uno, entonces ese es el número faltante.

```python
def find_missing(nums: list) -> int:
    last = nums[0]
    missing = []
    for i in range(1, len(nums)):
        if last + 1 != nums[i]:
            missing.append(last + 1)
        last = nums[i]
    
    return missing

print(enteros)
print(find_missing(enteros))
```

Puedes encontrar el código entero en [main.py](main.py).

## Resultados

```bash
python .\main.py
[1, 2, 3, 4, 5, 6, 7, 9, 10, 12]
[8, 11]
```
