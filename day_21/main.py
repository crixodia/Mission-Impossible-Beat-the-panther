import pprint


def transpose(mat: list) -> list:
    return [list(i) for i in zip(*mat)]


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Original matrix: ")
pprint.pprint(mat, width=20)
print("\nTransposed matrix: ")
pprint.pprint(transpose(mat), width=20)
