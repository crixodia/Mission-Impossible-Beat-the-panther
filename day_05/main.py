import sys
import re


def is_valid(password: str) -> bool:
    if len(password) < 8:
        return False

    have_number = re.search(r"[0-9]", password)
    have_space = re.search(r"\s", password)
    have_upper = re.search(r"[A-Z]", password)
    have_lower = re.search(r"[a-z]", password)

    return have_number and not have_space and have_upper and have_lower


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <password>")
        sys.exit(1)

    password = sys.argv[1]
    if is_valid(password):
        print("Valid password")
    else:
        print("Invalid password")
