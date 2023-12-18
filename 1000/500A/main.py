def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))

    c = 1
    while c < t:
        c += a[c - 1]

    if c == t:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    main()