import sys


def cesar(text: str, key: int, decrypt=False) -> str:
    factor = -1 if decrypt else 1
    cipher = map(lambda x: chr(ord(x) + factor * key), text)
    return "".join(cipher)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 main.py <texto: entre comillas> <clave: un número>")
        print("\tEjemplo: python3 main.py \"Hola mundo\" 5")
        sys.exit(1)

    text = sys.argv[1]
    key = int(sys.argv[2])
    # Desencriptar
    print(cesar(text, key//5, True))
