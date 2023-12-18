def method(year):
    m = year // 1000
    c = year % 1000 // 100
    d = year % 100 // 10
    n = year % 10

    if c == m:
        c += 1
        d = 0
        n = 0

    while d == c or d == m or n == d or n == c or n == m:
        if d == c or d == m:
            d += 1
            n = 0
        if n == d or n == c or n == m:
            n += 1
        if n == 10:
            n = 0
            d += 1
        if d >= 10:
            d = 0
            c += 1
        if c == 10:
            c = 0
            m += 1

    return m * 1000 + c * 100 + d * 10 + n


def main():
    y = int(input())
    print(method(y + 1))


if __name__ == "__main__":
    main()