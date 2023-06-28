# Día 12: Anagramas

Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Bool) según sean o no anagramas.

- Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.

- [Día 12: Anagramas](#día-12-anagramas)
  - [Solución](#solución)
  - [Ejecución](#ejecución)
  - [Resultados](#resultados)

## Solución

La solución es relativamente sencilla. Primero debemos comprobar que ambas palabras tengan la misma longitud, de lo contrario no pueden ser anagramas y que no sean la misma palabra. Luego, debemos comprobar que cada letra de la primera palabra esté en la segunda palabra.

```python
def is_anagram(word1: str, word2: str) -> bool:
    w1 = word1.upper()
    w2 = word2.upper()

    # Dos palabras de diferente longitud no son anagramas
    if len(w1) != len(w2):
        return False

    # Dos palabras iguales no son anagramas
    if w1 == w2:
        return False

    return sorted(w1) == sorted(w2)
```

Puedes encontrar el código completo en [main.py](main.py).

## Ejecución

Para ejecutar el programa desde la terminal:

```bash
python main.py "<palabra 1>" "<palabra 2>"
```

## Resultados

```bash
python main.py Mary Army
True
```

```bash
python main.py Mary Mary
False
```

```bash
python main.py Mary Mari
False
```

```bash
python main.py Mary Maryy
False
```
