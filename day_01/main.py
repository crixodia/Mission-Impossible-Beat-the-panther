import sys

SYMBOLS = "0123456789"


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


if __name__ == "__main__":
    if len(sys.argv) == 2:  # Validación de tarjetas de crédito
        print(f"{sys.argv[1]} -> {is_valid_card(sys.argv[1])}")
    else:
        print("Usage: python main.py <credit_card_number>")
