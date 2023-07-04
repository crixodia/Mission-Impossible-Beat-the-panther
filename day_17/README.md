# Día 17: Números romanos

Se le da una cadena y debe validar si es un número romano válido. Si es válido, imprima True. De lo contrario, escriba Falso. Intente crear una expresión regular para un número romano válido.

Reglas:

- EL número debe estar entre 1 y 3999 (ambos incluídos)

Input: CDXXI
Output: True

- [Día 17: Números romanos](#día-17-números-romanos)
  - [Contexto](#contexto)
  - [Solución](#solución)
  - [Ejecución](#ejecución)
  - [Resultados](#resultados)

## Contexto

Para este reto se utilizó la librería `re` de Python para crear una expresión regular que valide si la cadena de texto es un número romano válido.

## Solución

Se creó una función que recibe como parámetro la cadena de texto a validar, la cual retorna un valor booleano indicando si la cadena es un número romano válido o no.

```python
def is_valid_roman(number: str) -> bool:
    pattern = r"^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    return bool(re.match(pattern, number))
```

Puedes ver la solución completa [aquí](main.py).

## Ejecución

Para ejecutar el programa ejecuta:

```bash
python main.py <roman_number>
```

## Resultados

```bash
python .\main.py CDXXI
True
```

```bash
python .\main.py CDXXIIII
False
```

```bash
python .\main.py M       
True
```
