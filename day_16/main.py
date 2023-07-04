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
