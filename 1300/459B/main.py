def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    k = 0

    if t < min(a):
        print(0)
    else:
        startIndex = 0
        accumTime = 0
        k = 0
        for i in range(0, n):
            accumTime += a[i]
            if t < accumTime:
                accumTime -= a[startIndex]
                startIndex += 1
            else:
                k += 1

        print(k)


if __name__ == "__main__":
    main()