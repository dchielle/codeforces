def main():
    t = int(input())
    for _ in range(0, t):
        x, y = map(int, input().split())
        a, b = map(int, input().split())
        x, y = min(x, y), max(x, y)
        if x == 0 and y == 0:
            print(0)
        elif 2*a <= b:
            print(a*(x + y))
        else:
            print(b*x + a*(y -x))


if __name__ == "__main__":
    main()