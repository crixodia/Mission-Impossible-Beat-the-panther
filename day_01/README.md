# Día 1: Luhn

Eres un espía y acabas de extraer el número de tarjeta de crédito de María;
necesitas verificar si el número de tarjeta de crédito es válido antes de realizar una transacción e infiltrarte en la mansión del villano.


Escribe un programa que te permita validar números de tarjeta de crédito utilizando el algoritmo de Luhn.

- [Día 1: Luhn](#día-1-luhn)
  - [Contexto](#contexto)
  - [Solución](#solución)
  - [Ejecución](#ejecución)
  - [Resultados](#resultados)

## Contexto

Para esto, vamos a hacer uso del algoritmo de módulo 10 o también conocido como Fórmula de Luhn. Este algoritmo se aplica para validar diversidad de números de verificación, tarjetas de débito o crédito e incluso números IMEI.

Lo aplicaremos para validar un número de tarjeta de crédito:

| 4   | 5   | 3   | 9   | 3   | 1   | 9   | 5   | 0   | 3   | 4   | 3   | 6   | 4   | 6   | 7   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

El primer paso del algoritmo es duplicar cada segundo dígito empezando desde la derecha

| 4   | 5   | 3   | 9   | 3   | 1   | 9   | 5   | 0   | 3   | 4   | 3   | 6   | 4   | 6   | 7   |
| ----- | --- | ----- | --- | ----- | --- | ------ | --- | ----- | --- | ----- | --- | ------ | --- | ------ | --- |
| **8** | 5   | **6** | 9   | **6** | 1   | **18** | 5   | **0** | 3   | **8** | 3   | **12** | 4   | **12** | 7   |

Ahora, en este duplicado si el resultado es mayor que 9 le restamos 9

| 4     | 5   | 3     | 9   | 3     | 1   | 9      | 5   | 0     | 3   | 4     | 3   | 6      | 4   | 6      | 7   |
| ----- | --- | ----- | --- | ----- | --- | ------ | --- | ----- | --- | ----- | --- | ------ | --- | ------ | --- |
| **8** | 5   | **6** | 9   | **6** | 1   | **18** | 5   | **0** | 3   | **8** | 3   | **12** | 4   | **12** | 7   |
| **8** | 5   | **6** | 9   | **6** | 1   | **9**  | 5   | **0** | 3   | **8** | 3   | **3**  | 4   | **3**  | 7   |

Finalmente comprobaremos que la suma de todos los dígitos sea divisible para 10. Si esto ocurre, tenemos que indicarle al usuario que el número de tarjeta de crédito es válido, en caso contrario, le indicaremos que no es válido.

## Solución

Crearemos una función que reciba un número de tarjeta como string y lo valide.

Validaremos la longitud del número de tarjeta. Luego mapearemos los dígitos a un arreglo de enteros. Gracias a la notación slice de Python, podemos obtener los dígitos a duplicar y los que no de forma sencilla.

Luego usamos map para duplicar los dígitos y otro map para aplicar la fórmula de Luhn. Finalmente sumamos todos los dígitos y comprobamos si es divisible por 10.

```python
def is_valid_card(number: str) -> bool:
    number = number.strip().replace(" ", "")

    # Logitud de número de tarjeta de crédito
    if len(number) != 16:
        return False

    # Fórmula de Luhn
    digits = list(map(int, number))
    A = digits[::2]  # Dígitos con índice par
    B = digits[1::2]  # Dígitos con índice impar

    A = list(map(lambda x: 2*x, A))  # El factor se puede modificar
    A = list(map(lambda x: sum(divmod(x, 10)), A))

    return sum(list(A) + B) % 10 == 0
```

## Ejecución

Para ejecutar el programa debemos ejecutar el siguiente comando:

```bash
python main.py <card_number>
```

Donde `<card_number>` es el número de tarjeta de crédito a validar.

También puedes ejecutar las pruebas unitarias con el siguiente comando:

```bash
python test.py
```

## Resultados

Puedes encontrar el código completo [aquí](main.py).

Validamos un número de tarjeta de crédito.

```bash
python main.py "5387 0772 9033 3852"
python main.py "5387 0772 9033 3855"
```

Salida:

```bash
>> 5387 0772 9033 3852 -> False
>> 5387 0772 9033 3855 -> True
```

Autor: [crixodia](https://instagram.com/crixodia)
