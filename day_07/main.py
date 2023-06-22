import sys
import re


def is_valid_mail(email: str) -> bool:
    expr = r"^[a-zA-Z0-9\.]+@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+){1,2}$"
    return bool(re.match(expr, email))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <email>")
        sys.exit(1)

    email = sys.argv[1]
    if is_valid_mail(email):
        print("Valid email")
    else:
        print("Invalid email")
