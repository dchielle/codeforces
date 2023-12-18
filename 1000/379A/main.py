def main():
    a, b = map(int, input().split())

    q = a // b
    r = a % b

    h = a
    while q > 0:
        h += q
        a = r + q
        q = a // b
        r = a % b

    print(h)


if __name__ == "__main__":
    main()