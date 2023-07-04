# Día 8: Contar palabras

Escribe una función que tome una cadena de texto y cuente cuántas palabras hay en ella. Puedes asumir que las palabras están separadas por espacios y que no hay puntuación adicional.

- [Día 8: Contar palabras](#día-8-contar-palabras)
  - [Solución](#solución)
  - [Ejecución](#ejecución)
  - [Resultados](#resultados)

## Solución

Este reto es relativamente sencillo. Simplemte se crea una función que haga split a las palabras y cuente el número de elementos en el arreglo resultante.

```python
def count_words(text):
    return len(text.split()) 
```

Otra forma de hacerlo es recorrer la cadena de texto y contar los espacios.

```python
def count_words_iter(text):
    count = 0
    for c in text:
        if c == " ":
            count += 1
    return count + 1
```

Se asume que no hay saltos de línea ni tabuladores o puntuación adicional. Puedes encontrar la solución en [main.py](main.py).

## Ejecución

Para ejecutar el programa desde la terminal:

```bash
python3 count_words.py
```

## Resultados

```bash
python .\main.py
Enter text: Hola mundo Cruel.
There are 3 words in the text.
```

```bash
python .\main.py
Enter text: Pepito tiene una vaca.
There are 4 words in the text.
```
