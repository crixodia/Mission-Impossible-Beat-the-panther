import sys


def is_anagram(word1: str, word2: str) -> bool:
    w1 = word1.upper()
    w2 = word2.upper()

    # Dos palabras de diferente longitud no son anagramas
    if len(w1) != len(w2):
        return False

    # Dos palabras iguales no son anagramas
    if w1 == w2:
        return False

    return sorted(w1) == sorted(w2)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main.py <word1> <word2>")
        print("Usage: python main.py Mary Army")
        sys.exit(1)
    word1 = sys.argv[1]
    word2 = sys.argv[2]
    print(is_anagram(word1, word2))
