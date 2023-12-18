def method(year):
    m = year // 1000
    c = year % 1000 // 100
    d = year % 100 // 10
    n = year % 10

    if c == m:
        c += 1
        d = 0
        n = 0

    year = m * 1000 + c * 100 + d * 10 + n

    while len(set(str(year))) != 4:
        year += 1

    return year


def main():
    y = int(input())
    print(method(y + 1))


if __name__ == "__main__":
    main()