# Día 3: Número Mágico

El desafío consiste en encontrar el "número mágico" dentro de un rango específico.
Se te dará un rango de números enteros, desde un límite inferior hasta un límite superior (ambos inclusivos).
Tu tarea es encontrar el número mágico siguiendo las siguientes reglas:

1. El número mágico es un número impar.
2. El número mágico es divisible por 3.
3. La suma de los dígitos del número mágico es igual a 7.

Tu objetivo es encontrar el número mágico utilizando razonamiento lógico y operaciones matemáticas básicas.

## Contexto

Todo número divisible para 3 tiene una suma de dígitos que es divisible por 3. Esto hace que sea imposible que un número mágico sea divisible por 3 y tenga una suma de dígitos que sea 7. Y dado, que 7 no es divisible por 3 este problema **NO** tiene solución en este universo 😅.

## Solución

A pesar de la justificación anterior, se puede plantear la lógica del problema de la siguiente manera:

Se define una función que retorne la suma de los dígitos de un número entero.

```python
def sum_digits(number:int) -> int:
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return sum
```

Se define una función que obteenga los posibles números mágicos en un intervalo cerrado.

El programa completo se puede ver en [main.py](main.py).

```python
def get_magic_number(inf: int, sup: int) -> list:
    magic_numbers = []
    for number in range(inf, sup + 1):
        if number % 2 != 0 and number % 3 == 0 and sum_digits(number) == 7:
            magic_numbers.append(number)
    return magic_numbers
```

## Ejecución

```bash
python main.py <inf> <sup>
```

## Resultados

```bash
python main.py 1 10000
```

```bash
Es matemáticamente imposible pero el programa está ahí :v
Magic number: []
```

Autor: [crixodia](https://instagram.com/crixodia)
