def main():
    n, h = map(int, input().split())
    a = list(map(int, input().split()))
    width = 0
    for i in range(0, n):
        if a[i] > h:
            width += 1
        width += 1

    print(width)


if __name__ == "__main__":
    main()