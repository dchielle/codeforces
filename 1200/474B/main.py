def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    q = list(map(int, input().split()))

    qSorted = sorted(range(len(q)), key=lambda k: q[k])
    qPile = [0] * m
    k = 0
    accum = 0
    for i in range(0, n):
        accum += a[i]
        while k < m and q[qSorted[k]] <= accum:
            qPile[qSorted[k]] = i + 1
            k += 1

    for number in qPile:
        print(number)


if __name__ == "__main__":
    main()