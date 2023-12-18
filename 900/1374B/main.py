def main():
    t = int(input())
    for _ in range(0, t):
        n = int(input())
        i = 0
        while n != 1:
            if n % 3 != 0:
                break
            if n % 6 == 0:
                n /= 6
            else:
                n *= 2
            i += 1

        if n == 1:
            print(i)
        else:
            print(-1)


if __name__ == "__main__":
    main()