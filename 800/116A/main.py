def main():
    n = int(input())
    a = [0]*n           # passengers that exits the tram
    b = [0]*n           # passengers that enter the tram
    capacity = 0
    peopleIn = 0
    for i in range(0, n):
        a[i], b[i] = map(int, input().split())
        peopleIn += b[i] - a[i]
        if peopleIn > capacity:
            capacity = peopleIn

    print(capacity)


if __name__ == "__main__":
    main()