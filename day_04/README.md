# Día 4: Suma en Strings

El programador debe ingeniar una manera de ingresar una pareja de límites (inferior y superior).
Debe ser capaz de manejar varios casos que consisten en parejas de límites. (ejemplo 1-10,20-30,...)
Para cada caso, el programa debe encontrar y sumar todos los números pares dentro del rango especificado.
El programa debe mostrar en pantalla la suma de los números pares obtenida para cada caso.

- [Día 4: Suma en Strings](#día-4-suma-en-strings)
  - [Contexto](#contexto)
  - [Solución](#solución)
  - [Ejecución](#ejecución)
  - [Resultados](#resultados)

## Contexto

Para este caso se requieren manejo de cadenas de caracteres. Se usará `strip` y `split` para separar los límites de cada caso.

## Solución

Se define una función `parse_data` que recibe una cadena de texto con el  formato `1-10,20-30` y retorna una lista de tuplas con los límites de cada caso. Primero se eliminan los espacios en blanco y se separan los casos por comas. Luego se separan los límites de cada caso por el guión y se convierten a enteros.

```python
def parse_data(data: str) -> list:
    data = data.replace(" ", "").strip()
    I = [x for x in data.split(",")]
    I = [x.split("-") for x in I]
    return [(int(y[0]), int(y[1])) for y in I]
```

Luego, se define una función `sum_even` que recibe una tupla con los límites de un caso y retorna la suma de los números pares dentro del rango especificado. Se usa una comprensión de lista para generar los números dentro del rango y se filtran los números pares. Finalmente se retorna la suma de los números pares.

```python
def get_sum_even(I: list) -> int:
    return sum([x for x in range(I[0], I[1] + 1) if x % 2 == 0])
```

Finalmente, se define una función `main` que recibe una cadena de texto con el formato `1-10,20-30,...` y ejecuta las funciones anteriores. Primero se parsea la cadena de texto y se obtienen los límites de cada caso. Luego, se itera sobre los límites de cada caso y se obtiene la suma de los números pares dentro del rango especificado. Finalmente, se imprime en pantalla la suma de los números pares obtenida para cada caso.

```python
def main(data: str):
    parsed = parse_data(data)
    sums = map(get_sum_even, parsed)

    for i, x in enumerate(sums):
        print(f"Suma de pares contenidos en {parsed[i]}", "es", x)
```

Puedes ver el código completo en [main.py](main.py).

## Ejecución

Para ejecutar el programa:

```bash
python main.py
```

## Resultados

`python main.py "1-10, 20-30, 35-45"`

Retorna:

```bash
Suma de pares contenidos en (1, 10) es 30
Suma de pares contenidos en (20, 30) es 150
Suma de pares contenidos en (35, 45) es 200
```

`python main.py "100-200"`

Retorna:

```bash
Suma de pares contenidos en (100, 200) es 7650
```
