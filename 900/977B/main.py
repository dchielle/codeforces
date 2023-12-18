def main():
    n = int(input())
    s = list(input())
    twoGrams = []
    for i in range(1, n):
        twoGrams.append(s[i - 1] + s[i])

    unique = set(twoGrams)
    count = []
    for item in unique:
        count.append(twoGrams.count(item))

    idx = count.index(max(count))
    print(list(unique)[idx])


if __name__ == "__main__":
    main()