# Día 22: Espías Ecuatorianos

Uno de los espías es ecuatoriano, necesitamos conocer si en verdad es una cédul real y la provincia a la que pertenece.

- [Día 22: Espías Ecuatorianos](#día-22-espías-ecuatorianos)
  - [Contexto](#contexto)
  - [Solución](#solución)
  - [Resultados](#resultados)

## Contexto

Para resolver este reto podemos tomar el algoritmo de Luhn que se resolvió en el día uno [aquí](../day_01/) y aplicarlo a la cédula ecuatoriana.

Pasra saber a que provincia pertenece simplementa tomamos los dos primeros dígitos y los comparamos con la siguiente tabla:

| Código | Provincia |
| ------ | --------- |
| 01     | Azuay     |
| 02     | Bolívar   |
| 03     | Cañar     |
| 04     | Carchi    |
| 05     | Cotopaxi  |
| 06     | Chimborazo|
| 07     | El Oro    |
| 08     | Esmeraldas|
| 09     | Guayas    |
| 10     | Imbabura  |
| 11     | Loja      |
| 12     | Los Ríos  |
| 13     | Manabí    |
| 14     | Morona Santiago|
| 15     | Napo      |
| 16     | Pastaza   |
| 17     | Pichincha |
| 18     | Tungurahua|
| 19     | Zamora Chinchipe|
| 20     | Galápagos |
| 21     | Sucumbíos |
| 22     | Orellana  |
| 23     | Santo Domingo de los Tsáchilas|
| 24     | Santa Elena|

Esta tabla se representará en un diccionario de python de la siguiente manera:

## Solución

```python
def is_valid_ci(number: str) -> bool:
    number = number.strip().replace(" ", "")

    # Logitud de número de cédula
    if len(number) != 10:
        return False

    # Fórmula de Luhn
    digits = list(map(int, number))
    A = digits[::2]  # Dígitos con índice par
    B = digits[1::2]  # Dígitos con índice impar

    A = list(map(lambda x: 2*x, A))  # El factor se puede modificar
    A = list(map(lambda x: sum(divmod(x, 10)), A))

    return sum(list(A) + B) % 10 == 0
```

El código completo lo puedes encontrar [aquí](./main.py).

## Resultados

```bash
python .\main.py
Ingrese su número de cédula: 1308333011
Su número de cédula no es válido.
(env) PS D:\Repositories\Mission-Impossible-Beat-the-panther\day_22> python .\main.py
Ingrese su número de cédula: 130[xxxxx]10
Usted es de la provincia de Manabí
