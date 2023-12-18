def main():
    t = int(input())
    for _ in range(0, t):
        n = int(input())
        a = list(map(int, input().split()))
        b = {}
        for i in range(0, n):
            if a[i] - i in b:
                b[a[i] - i] += [i]
            else:
                b[a[i] - i] = [i]

        count = 0
        for key in b:
            k = len(b[key]) - 1
            count += k*(k+1)/2

        print(int(count))


if __name__ == "__main__":
    main()