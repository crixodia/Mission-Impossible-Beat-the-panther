# Día 5: Validación de Contraseña

Hackeaste la contraseña del laboratorio secreto del villano. Escribe un programa que te permita verificar si una contraseña cumple con lo siguiente:

1. La contraseña debe tener al menos 8 caracteres.
2. La contraseña debe contener al menos una letra mayúscula y una letra minúscula.
3. La contraseña debe contener al menos un número.
4. La contraseña no debe contener espacios en blanco.

- [Día 5: Validación de Contraseña](#día-5-validación-de-contraseña)
  - [Contexto](#contexto)
  - [Solución](#solución)
  - [Ejecución](#ejecución)
  - [Resultados](#resultados)

## Contexto

Se puede abordar este problema desde varias perspectivas, pero la más sencilla es utilizar expresiones regulares. En Python, las expresiones regulares se pueden utilizar a través del módulo `re`. Para utilizarlo, se debe importar el módulo y luego utilizar la función `re.match()`.

## Solución

Se crea una función que reciba un string y que retorne `True` si el string cumple con las condiciones de la contraseña y `False` en caso contrario. Para ello, se utiliza la función `re.match()`. La longitud de la contraseña se puede verificar con la función `len()`. En la siguiente tabla se muestran las expresiones regulares utilizadas para verificar las condiciones de la contraseña.

| Condición                                                                       | Expresión Regular |
| :------------------------------------------------------------------------------ | :---------------- |
| La contraseña debe contener al menos una letra mayúscula y una letra minúscula. | `[A-Z]` y `[a-z]` |
| La contraseña debe contener al menos un número.                                 | `[0-9]`           |
| La contraseña no debe contener espacios en blanco.                              | `"\s"`            |

```python
def is_valid(password: str) -> bool:
    if len(password) < 8:
        return False

    have_number = re.search(r"[0-9]", password)
    have_space = re.search(r"\s", password)
    have_upper = re.search(r"[A-Z]", password)
    have_lower = re.search(r"[a-z]", password)

    return have_number and not have_space and have_upper and have_lower
```

El código completo se encuentra en [main.py](main.py).

## Ejecución

Para ejecutar el programa, se debe ejecutar el siguiente comando:

```bash
python main.py <password>
```

## Resultados

Los resultados se muestran a continuación.

```bash
python main.py "12345678"
Invalid password

python main.py "12345678a"
Invalid password

python main.py "Passw0rd"
Valid password

python main.py "12345678aA"
Valid password

python main.py "12345678aA "
Invalid password
```

[crixodia](https://instagram.com/crixodia)
