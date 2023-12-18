def main():
    n, m = map(int, input().split())
    s = input().split()
    prices = [eval(i) for i in s]
    prices.sort()
    money = 0
    for i in range(0, m):
        if prices[i] < 0:
            money += prices[i]
        else:
            break

    print(-1*money)


if __name__ == "__main__":
    main()