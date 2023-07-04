# Día 16: Peluches con Mensajes

Manejas un negocio de peluches con mensajes. Un dia, te han pedido fabricar un peluche con las siguientes especificaciones:

- El tamaño del peluche debe ser N X M. (N es un número natural impar y M es 3 veces N).
- El diseño debe tener escrito 'BIENVENIDO' en el centro.
- El patrón de diseño solo debe usar los siguientes caracteres (|, ., -)

- [Día 16: Peluches con Mensajes](#día-16-peluches-con-mensajes)
  - [Solución](#solución)
  - [Ejecución](#ejecución)
  - [Resultados](#resultados)
  
## Solución

```python
def crear_peluche(n, m):
    if n % 2 == 0:
        print("El valor de N debe ser un número impar.")
        return

    if m != 3 * n:
        print("El valor de M debe ser 3 veces el valor de N.")
        return

    mensaje = "BIENV.ENIDO"
    ancho_patron = len(mensaje) + 2

    for i in range(n):
        if i == n // 2:
            print(
                "|"
                + "." * ((m - ancho_patron) // 2)
                + mensaje
                + "." * ((m - ancho_patron) // 2)
                + "|"
            )
        else:
            print("|" + "-" * (m - 2) + "|")


n = 9
m = 27

crear_peluche(n, m)

```

Puedes encontrar el código [aquí](day_16/main.py).

## Resultados

```bash
| ------------------------- |
| ------------------------- |
| ------------------------- |
| ------------------------- |
| .......BIENV.ENIDO....... |
| ------------------------- |
| ------------------------- |
| ------------------------- |
| ------------------------- |
```
