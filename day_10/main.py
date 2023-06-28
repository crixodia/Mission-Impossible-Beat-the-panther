from itertools import permutations
import sys
import pprint


def gen_words(chars: str) -> list:
    words = ["".join(x) for x in permutations(chars, len(chars))]
    return set(words)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python main.py <chars>")
        exit(1)
    chars = sys.argv[1]
    words = gen_words(chars)
    pprint.pprint(words, compact=True)
    print(f"Generated {len(words)} words")
