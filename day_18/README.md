# Día 18: Pasaportes

Se le pide que se asegure de que el nombre y los apellidos de las personas empiecen por mayúsculas en sus pasaportes. Por ejemplo, july herrera debe escribirse correctamente en mayúsculas como July Herrera. Dado un nombre completo, su tarea consiste en escribir el nombre en mayúsculas correctamente.

- [Día 18: Pasaportes](#día-18-pasaportes)
  - [Solución](#solución)
  - [Ejecución](#ejecución)

## Solución

Simplemente se recorre el string y se va cambiando a mayúsculas el primer caracter de cada palabra.

```python
nombre = input("Ingresa tu nombre y apellido: ")
print(nombre.lower().title())
```

Puedes econtrar el código completo en [main.py](main.py).

## Ejecución

```bash
python main.py
Ingresa tu nombre y apellido: cristian basidas
Cristian Basidas
```
