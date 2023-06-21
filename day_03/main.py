import sys

def sum_digits(number:int) -> int:
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return sum


def get_magic_number(inf: int, sup: int) -> list:
    magic_numbers = []
    for number in range(inf, sup + 1):
        if number % 2 != 0 and number % 3 == 0 and sum_digits(number) == 7:
            magic_numbers.append(number)
    return magic_numbers

    
if __name__ == "__main__":
    if len(sys.argv) == 3:
        inf = int(sys.argv[1])
        sup = int(sys.argv[2])
        magic_number = get_magic_number(inf, sup)
        print("Es matemáticamente imposible pero el programa está ahí :v")
        print(f"Magic number: {magic_number}")
    else:
        print("Usage: python main.py <inf> <sup>")