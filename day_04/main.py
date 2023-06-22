import sys


def parse_data(data: str) -> list:
    data = data.replace(" ", "").strip()
    I = [x for x in data.split(",")]
    I = [x.split("-") for x in I]
    return [(int(y[0]), int(y[1])) for y in I]


def get_sum_even(I: list) -> int:
    return sum([x for x in range(I[0], I[1] + 1) if x % 2 == 0])


def main(data: str):
    parsed = parse_data(data)
    sums = map(get_sum_even, parsed)

    for i, x in enumerate(sums):
        print(f"Suma de pares contenidos en {parsed[i]}", "es", x)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Usage: python main.py <data>")
        print('Example: python main.py "1-10, 20-30, 35-45"')
