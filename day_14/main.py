import sys


def winner_turtle(t1: int, t2: int, t3: int) -> str:
    if t1 > t2 and t1 > t3:
        return "Turtle 1"
    elif t2 > t1 and t2 > t3:
        return "Turtle 2"
    elif t3 > t1 and t3 > t2:
        return "Turtle 3"
    else:
        return "Draw"


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python main.py <turtle1> <turtle2> <turtle3>")
        exit(1)

    turtle1 = int(sys.argv[1])
    turtle2 = int(sys.argv[2])
    turtle3 = int(sys.argv[3])

    print(winner_turtle(turtle1, turtle2, turtle3))
