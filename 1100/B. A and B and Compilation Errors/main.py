def main():
    n = int(input())
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()))
    c = sorted(map(int, input().split()))

    b.append(0)
    c.append(0)
    c.append(0)

    for i in range(0, n):
        if b[i] != a[i]:
            errorB = a[i]
            break

    for i in range(0, n):
        if c[i] != b[i]:
            errorC = b[i]
            break

    print(errorB)
    print(errorC)


if __name__ == "__main__":
    main()