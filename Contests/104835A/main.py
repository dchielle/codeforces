def sumFirstIntegers(n):
    return n * (n + 1) // 2


def main():
    t = int(input())
    for _ in range(0, t):
        L, N = map(int, input().split())
        print( sumFirstIntegers(L + N - 1) - sumFirstIntegers(L - 1) )


if __name__ == "__main__":
    main()