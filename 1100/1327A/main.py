def main():
    t = int(input())
    for _ in range(0, t):
        n, k = map(int, input().split())
        if n < k ** 2:
            print('NO')
            continue
        if n % 2 == 0 and k % 2 == 1:
            print('NO')
            continue
        if n % 2 == 1 and k % 2 == 0:
            print('NO')
            continue
        print('YES')


if __name__ == "__main__":
    main()