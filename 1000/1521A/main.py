def main():
    t = int(input())
    for _ in range(0, t):
        A, B = map(int, input().split())
        if B == 1:
            print('NO')
        else:
            x = A * B
            y = A
            z = x + y
            print('YES')
            print(x, y, z)


if __name__ == "__main__":
    main()