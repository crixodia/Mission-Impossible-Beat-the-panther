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


def get_state(ci: str) -> str:
    diccionario = {
        "01": "Azuay",
        "02": "Bolívar",
        "03": "Cañar",
        "04": "Carchi",
        "05": "Cotopaxi",
        "06": "Chimborazo",
        "07": "El Oro",
        "08": "Esmeraldas",
        "09": "Guayas",
        "10": "Imbabura",
        "11": "Loja",
        "12": "Los Ríos",
        "13": "Manabí",
        "14": "Morona Santiago",
        "15": "Napo",
        "16": "Pastaza",
        "17": "Pichincha",
        "18": "Tungurahua",
        "19": "Zamora Chinchipe",
        "20": "Galápagos",
        "21": "Sucumbíos",
        "22": "Orellana",
        "23": "Santo Domingo de los Tsáchilas",
        "24": "Santa Elena"
    }

    return diccionario[ci[0:2]]


if __name__ == "__main__":
    ci = input("Ingrese su número de cédula: ")

    if is_valid_ci(ci):
        print("Usted es de la provincia de", get_state(ci))
    else:
        print("Su número de cédula no es válido.")
