# Días 2: Conversor de Unidades

Te encuentras realizando una misión en China y necesitas convertir unidades de medida para evitar ser descubierto. Escribe un programa que te permita convertir entre diferentes unidades de medida, como centímetros a pulgadas, kilómetros a millas, etc.

- [Días 2: Conversor de Unidades](#días-2-conversor-de-unidades)
  - [Contexto](#contexto)
  - [Solución](#solución)
  - [Ejecución](#ejecución)
  - [Resultados](#resultados)

## Contexto

Para resolver este reto se usó el archivo [conversion_factors.json](/day_02/conversion_factors.json) como base de datos de prefijos y unidades de medida con el fin de crear un conversor casi completo de unidades. Este archivo fue tomado de [unitdb](https://github.com/GhostWrench/unitdb/tree/trunk).

## Solución

Se carga el contenido del archivo JSON conversion_factors.json que contiene los factores de conversión necesarios.

```python
def units_convert(value, prefix, unit, to_prefix, to_unit):
    conversion_factors = json.load(open('conversion_factors.json'))
```

Se definen dos diccionarios, prefixes y units, que se inicializan con un diccionario vacío {} como valor predeterminado en caso de que no se encuentren en el archivo JSON.

```python
prefixes = conversion_factors.get("prefixes", {})
units = conversion_factors.get("units", {})
```

Se realizan las siguientes comprobaciones de validez de las unidades de conversión:

```python
if prefix not in prefixes and prefix:
    print(f"Error: prefix {prefix} not found")
    sys.exit(1)

if unit not in units:
    print(f"Error: unit {unit} not found")
    sys.exit(1)

if to_prefix not in prefixes and to_prefix:
    print(f"Error: prefix {to_prefix} not found")
    sys.exit(1)

if to_unit not in units:
    print(f"Error: unit {to_unit} not found")
    sys.exit(1)

```

Se verifica si las unidades unit y to_unit tienen la misma categoría. Esto se hace comparando los valores de la clave "category" en los diccionarios correspondientes dentro del diccionario units. Si las categorías no coinciden, se imprime un mensaje de error indicando que las unidades no son compatibles y se termina el programa.

```python
if units.get(unit, {}).get("category") != units.get(to_unit, {}).get("category"):
    print(f"Error: units {unit} and {to_unit} are not compatible")
    sys.exit(1)

```

Se obtienen los factores de escala necesarios para la conversión utilizando los diccionarios prefixes y units. Si no se encuentra un factor de escala para un prefijo o una unidad en particular, se utiliza un valor predeterminado de 1.

```python
to_prefix_scale = float(prefixes.get(to_prefix, {}).get("scale", 1))
from_prefix_scale = float(prefixes.get(prefix, {}).get("scale", 1))
to_scale = float(units.get(to_unit, {}).get("scale", 1))
from_scale = float(units.get(unit, {}).get("scale", 1))
```

Se realiza la conversión de unidades aplicando los factores de escala adecuados a los valores proporcionados.

```python
return (value * from_scale * from_prefix_scale) / (to_scale * to_prefix_scale)
```

Puedes encontrar el código completo [aquí](/day_02/main.py).

## Ejecución

Para ejecutar el programa debemos ejecutar el siguiente comando:

```bash
python main.py
```

Lo que a continuación solicitará los siguientes datos:

```bash
Enter value [float]: 1
Enter prefix [str]: k
Enter unit [str]: m
Prefix to convert [str]: 
Unit to convert [str]: mi
```

Lo que nos dará como resultado:

```bash
1.0 km = 0.621371192237334 mi
```

## Resultados

Convertir 1 km a mi:

```bash
Enter value [float]: 1
Enter prefix [str]: k
Enter unit [str]: m
Prefix to convert [str]: 
Unit to convert [str]: mi
1.0 km = 0.621371192237334 mi
```

Convertir de yd a m:

```bash
Enter value [float]: 1
Enter prefix [str]:
Enter unit [str]: yd
Prefix to convert [str]:
Unit to convert [str]: m
1.0 yd = 0.9144 m
```

NOTA: Si la unidad no tiene prefijo, se debe dejar en blanco el campo de prefijo.

Autor: [crixodia](https://instagram.com/crixodia)
