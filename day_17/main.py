import re
import sys



def is_valid_roman(number: str) -> bool:
    pattern = r"^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    return bool(re.match(pattern, number))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <roman_number>")
        sys.exit(1)
    roman_number = sys.argv[1]
    print(is_valid_roman(roman_number))
