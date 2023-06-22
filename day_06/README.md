# Día 6: Matrices

El desafío consiste en escribir un programa que tome un número entero positivo n y genere una matriz de tamaño n x n que contenga una espiral ascendente de números,comenzando desde 1 y siguiendo un patrón en sentido horario.

- [Día 6: Matrices](#día-6-matrices)
  - [Solución](#solución)
  - [Ejecución](#ejecución)
  - [Resultados](#resultados)

## Solución

Se crea una matriz vacía de tamaño `n` y luego utiliza variables para controlar la posición actual en la matriz y la dirección de movimiento. A medida que itera desde 1 hasta `n * n`, se asigna el número actual en la posición correspondiente de la matriz. Si alcanza los límites de la matriz o la siguiente posición no está vacía, cambia la dirección de movimiento.

```python
def spiral_matrix(n):
    M = [[0] * n for _ in range(n)]

    i, j = 0, 0
    di, dj = 0, 1

    for num in range(1, n * n + 1):
        M[i][j] = num

        if (
            i + di >= n
            or j + dj >= n
            or i + di < 0
            or j + dj < 0
            or M[i + di][j + dj] != 0
        ):
            di, dj = dj, -di

        i += di
        j += dj

    return M

```

Puedes encontrar el código completo en [main.py](main.py).

## Ejecución

Para ejecutar el programa, se debe ejecutar el siguiente comando:

```bash
python main.py <n>
```

## Resultados

```bash
python main.py 1
   1
```

```bash
python main.py 2
   1   2
   4   3
```

```bash
python main.py 3
   1   2   3
   8   9   4
   7   6   5
```

```bash
python main.py 4
   1   2   3   4
  12  13  14   5
  11  16  15   6
  10   9   8   7
```

```bash
python main.py 5
   1   2   3   4   5
  16  17  18  19   6
  15  24  25  20   7
  14  23  22  21   8
  13  12  11  10   9
```

```bash
python main.py 10
  1   2   3   4   5   6   7   8   9  10
  36  37  38  39  40  41  42  43  44  11
  35  64  65  66  67  68  69  70  45  12
  34  63  84  85  86  87  88  71  46  13
  33  62  83  96  97  98  89  72  47  14
  32  61  82  95 100  99  90  73  48  15
  31  60  81  94  93  92  91  74  49  16
  30  59  80  79  78  77  76  75  50  17
  29  58  57  56  55  54  53  52  51  18
  28  27  26  25  24  23  22  21  20  19
```
