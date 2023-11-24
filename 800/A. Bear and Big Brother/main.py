import math


def main():
    a, b = map(int, input().split())
    t = math.log(b/a, 3/2)
    print(int(t) + 1)


if __name__ == "__main__":
    main()