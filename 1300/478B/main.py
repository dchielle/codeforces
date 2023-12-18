def main():
    n, m = map(int, input().split())

    d = n - m
    maxF = d * (d + 1) // 2

    if m == 1:
        minF = maxF
    else:
        q = n // m
        r = n % m
        minF = (m - r) * (q - 1) * q // 2 + r * (q + 1) * q // 2

    print(minF, maxF)


if __name__ == "__main__":
    main()