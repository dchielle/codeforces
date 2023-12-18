def main():
    k = int(input())
    a = list(map(int, input().split()))

    s = 0
    m = 0
    while s < k and len(a) > 0:
        max_idx = a.index(max(a))
        s += a[max_idx]
        m += 1
        del a[max_idx]

    if s >= k:
        print(m)
    else:
        print(-1)


if __name__ == "__main__":
    main()