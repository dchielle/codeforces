def main():
    n, m = map(int, input().split())
    s = input().split()
    s = [eval(i) for i in s]

    for _ in range(0, m):
        l = int(input())

        numbers = s[l - 1:n]
        repeated = []
        for i in range(l - 1, n):
            k = numbers.count(s[i])
            repeated.append(1/k)

        print(int(sum(repeated)))


if __name__ == "__main__":
    main()