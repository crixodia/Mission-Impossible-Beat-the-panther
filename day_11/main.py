import sys

KEY = "MURCIELAGO"
REPLACEMENT = "0123456789"

MAP = dict(zip(REPLACEMENT, KEY))


def decrypt(encrypted_text):
    return "".join(MAP.get(c, c) for c in encrypted_text)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <encrypted_text>")
        sys.exit(1)
    encrypted_text = sys.argv[1]
    print(decrypt(encrypted_text).capitalize())
