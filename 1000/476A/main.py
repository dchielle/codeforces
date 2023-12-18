def main():
    n, m = map(int, input().split())

    if n < m:
        print(-1)
        return

    k = n // 2
    if n % 2 == 0 and k % m == 0:
        print( k )
    else:
        print( k + m - k % m)


if __name__ == "__main__":
    main()