from collections import Counter
from random import randint

def get_duplicated(elements:list) -> list:
    C = Counter(elements)
    return [k for k, v in C.items() if v > 1]

if __name__ == "__main__":
    elements = [randint(1, 10) for _ in range(20)]
    duplicated = get_duplicated(elements)
    print("Original: ", elements)
    print("Duplicated: ", duplicated)