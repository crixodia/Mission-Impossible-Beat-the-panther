import sys


def spiral_matrix(n):
    M = [[0] * n for _ in range(n)]

    i, j = 0, 0
    di, dj = 0, 1

    for num in range(1, n * n + 1):
        M[i][j] = num

        if (
            i + di >= n
            or j + dj >= n
            or i + di < 0
            or j + dj < 0
            or M[i + di][j + dj] != 0
        ):
            di, dj = dj, -di

        i += di
        j += dj

    return M


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <size>")
        exit(1)

    n = int(sys.argv[1])
    M = spiral_matrix(n)

    for i in range(n):
        for j in range(n):
            print("{:4d}".format(M[i][j]), end="")
        print()
