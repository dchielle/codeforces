def main():
    k, n, w = map(int, input().split())
    price = k * w * (w+1) // 2
    if price < n:
        print(0)
    else:
        print(price - n)


if __name__ == "__main__":
    main()