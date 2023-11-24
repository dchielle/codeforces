def main():
    n, t = map(int, input().split())

    if n == 1:
        if t == 10:
            print(-1)
        else:
            print(t)
    else:
        if t == 10:
            print(10**(n-1))
        else:
            print(t*10**(n-1))


if __name__ == "__main__":
    main()