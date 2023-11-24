def main():
    s = input()
    m = int(input())
    for _ in range(0, m):
        l, r = map(int, input().split())

        previous = s[l-1]
        count = 0
        for i in range(l, r):
            if previous == s[i]:
                count += 1

            previous = s[i]

        print(count)


if __name__ == "__main__":
    main()