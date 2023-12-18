def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    i = 0
    while sum(a) > 0:
        a[i] -= min(a[i], m)

        if i == n - 1 and sum(a) > 0:
            i = 0
        else:
            i += 1

    print(i)


if __name__ == "__main__":
    main()