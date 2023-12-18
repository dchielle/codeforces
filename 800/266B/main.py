def main():
    n, t = map(int, input().split())
    s = list(input())

    for j in range(0, t):
        i = 1
        while i < n:
            if s[i - 1] == 'B' and s[i] == 'G':
                s[i - 1], s[i] = 'G', 'B'
                i += 1
            i += 1

    print(''.join(s))


if __name__ == "__main__":
    main()