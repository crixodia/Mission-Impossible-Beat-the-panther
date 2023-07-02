# Día 14: La Carrera de Tortugas

Historia: En una carrera de tortugas, cada tortuga tiene un número asignado que indica su velocidad. Queremos determinar qué tortuga ganó la carrera.

Instrucciones:

1. Escribe un programa que tome como entrada los números de velocidad de tres tortugas.
2. El programa debe comparar los números de velocidad y determinar cuál es el más grande.
3. Imprime el número de la tortuga ganadora.

- [Día 14: La Carrera de Tortugas](#día-14-la-carrera-de-tortugas)
  - [Contexto](#contexto)
  - [Solución](#solución)
  - [Ejecución](#ejecución)
  - [Resultados](#resultados)

## Contexto

Para resolver este reto simplementa hay que comparar los números y determinar el máximo de los 3.

## Solución

Definimos una función que recibe los 3 números y retorna un string de la tortuga ganadora.

```python
def winner_turtle(t1: int, t2: int, t3: int) -> str:
    if t1 > t2 and t1 > t3:
        return "Turtle 1"
    elif t2 > t1 and t2 > t3:
        return "Turtle 2"
    elif t3 > t1 and t3 > t2:
        return "Turtle 3"
    else:
        return "Draw"

```

Puedes ver el código completo en [main.py](main.py)

## Ejecución

Para ejecutar el programa desde la terminal:

```bash
python main.py <t1> <t2> <t3>
```

## Resultados

```bash
python .\main.py 12 14 15
Turtle 3
```

```bash
python .\main.py 12 12 12
Draw
```

```bash
python .\main.py 11 19 12
Turtle 2
```