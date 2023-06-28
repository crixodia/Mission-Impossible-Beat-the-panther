# Día 11: Encriptación

Un doctor en ENCRIPTACIÓN ha sido asesinado, su obsesión siempre fueron los MURCIELAGOS quienes tienen algo que ver en sus ultimas palabras su carta final fue una frase dirigida a una persona llamada TRISTEZA: `T24st5z7 S9y y9 d5 n15v9 H735 t450p9 q15 n9s v509s N9 p92q15 q14527 p529 b15n9 1st5d s450p25 05 q14s9 0as`.

- El código comienza desde el 0 hasta el 9

- [Día 11: Encriptación](#día-11-encriptación)
  - [Contexto](#contexto)
  - [Solución](#solución)
  - [Ejecución](#ejecución)
  - [Resultados](#resultados)

## Contexto

La solución es relativamente sencilla. Mapearemos la plabra MURCIELAGO con los números del 0 al 9 y luego reemplazaremos cada número por su respectiva letra.

## Solución

Crearemos un diccionario con la palabra MURCIELAGO y luego reemplazaremos cada número por su respectiva letra.

```python
KEY = "MURCIELAGO"
REPLACEMENT = "0123456789"

MAP = dict(zip(REPLACEMENT, KEY))
```

Definimos una función que reciba un texto y reemplace cada número por su respectiva letra.

```python
def decrypt(encrypted_text):
    return "".join(MAP.get(c, c) for c in encrypted_text)
```

Puedes encontrar el código completo en [main.py](main.py).

## Ejecución

Para ejecutar el programa desde la terminal:

```bash
python main.py "<texto encriptado>"
```

## Resultados

Usando el ejemplo del enunciado:

```bash
python main.py "T24st5z7 S9y y9 d5 n15v9 H735 t450p9 q15 n9s v509s N9 p92q15 q14527 p529 b15n9 1st5d s450p25 05 q14s9 0as"
```

Obtenemos:

```bash
Tristeza soy yo de nuevo hace tiempo que nos vemos no porque quiera pero bueno usted siempre me quiso mas
```
