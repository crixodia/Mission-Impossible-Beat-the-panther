# Día 13: El Tesoro Escondido

Eres un valiente explorador en busca de un tesoro escondido en una isla misteriosa. Para encontrar el tesoro, debes seguir una serie de instrucciones y llegar al destino final.

Instrucciones:

- Partiendo desde tu posición inicial (0, 0), sigue las siguientes coordenadas: (2, 3), (-1, 5), (4, -2).
- Calcula la posición final sumando todas las coordenadas.
- Tu tarea es escribir un programa que tome estas instrucciones y calcule la posición final del tesoro.

- [Día 13: El tesoro escondido](#día-13-el-tesoro-escondido)
  - [Contexto](#contexto)
  - [Solución](#solución)
  - [Ejecución](#ejecución)
  - [Resultados](#resultados)

## Contexto

Para este reto simplemente sumamos las componentes de las coordenadas como si de vectores se trataran.

## Solución

Definimos una función que realice el problema de forma general, es decir, que reciba una lista de coordenadas y devuelva suma.

```python
def sumar_coordenadas(coordenadas):
    x = 0
    y = 0
    for coordenada in coordenadas:
        x += coordenada[0]
        y += coordenada[1]
    return x, y
```

El co digo completo se encuentra en [main.py](main.py).

## Ejecución

Para ejecutar el programa, ejecuta `python main.py` desde la carpeta `day_13`.

## Resultados

```bash
$ python main.py
(5, 6)
```
