# Día 7: Validación de Correo Electrónico

Crea una función que verifique si una cadena dada representa una dirección de correo electrónico válida. La dirección de correo electrónico debe tener el formato "<nombre@dominio.extension>" y cumplir con algunas reglas básicas, como tener al menos un carácter antes y después del símbolo "@".

- [Día 7: Validación de Correo Electrónico](#día-7-validación-de-correo-electrónico)
  - [Contexto](#contexto)
  - [Solución](#solución)
  - [Ejecución](#ejecución)
  - [Resultados](#resultados)

## Contexto

Para este reto se pueden usar expresiones regulares.

## Solución

A continuación se muestra una explicación de la expresión regular en forma de una tabla:

| Símbolo          | Descripción                                                                                                                          |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| ^                | Coincide con el inicio de la cadena.                                                                                                 |
| [a-zA-Z0-9\.]+   | Coincide con uno o más caracteres alfanuméricos (letras mayúsculas, letras minúsculas o dígitos) antes del símbolo "@".              |
| @                | Coincide con el símbolo "@" literal.                                                                                                 |
| [a-zA-Z0-9]+     | Coincide con uno o más caracteres alfanuméricos después del símbolo "@".                                                             |
| (\.[a-zA-Z0-9]+) | Grupo de captura que coincide con un punto seguido de uno o más caracteres alfanuméricos. Este grupo puede repetirse de 1 a 2 veces. |
| {1,2}            | Cuantificador que indica que el grupo anterior (el grupo de captura) debe repetirse de 1 a 2 veces.                                  |
| $                | Coincide con el final de la cadena.                                                                                                  |

Esta expresión cumple con las siguientes reglas:

1. Deben comenzar con uno o más caracteres alfanuméricos (letras mayúsculas, letras minúsculas o dígitos).
2. Después del símbolo "@" debe haber uno o más caracteres alfanuméricos.
3. Después del símbolo "@" puede haber uno o dos grupos que consistan en un punto seguido de uno o más caracteres alfanuméricos.

Esta validación se realiza con la siguiente función:

```python
def is_valid_mail(email: str) -> bool:
    expr = r"^[a-zA-Z0-9\.]+@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+){1,2}$"
    return bool(re.match(expr, email))
```

Puedes encontrar el código de la solución en el archivo [main.py](main.py).

## Ejecución

Para ejecutar el programa debes ejecutar el siguiente comando:

```bash
python main.py "<email@dominio.com>"
```

## Resultados

```bash
python .\main.py example123@example.com
Valid email
```

```bash
python .\main.py john.doe@example.co.uk
Valid email
```

```bash
python .\main.py "@example.com"
Invalid email
```

```bash
python .\main.py "john.doe@example..com"
Invalid email
```
