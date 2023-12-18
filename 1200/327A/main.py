def main():
    n = int(input())
    a = list(map(int, input().split()))

    somaBase = sum(a)
    somaMax = sum(a)
    change = False
    for i in range(0, n):
        saldoA = 0
        saldoB = 0
        for j in range(i, n):
            saldoA += a[j]
            saldoB -= a[j] - 1
            soma = somaBase + saldoB - saldoA
            if soma > somaMax:
                somaMax = soma
                change = True
    if change:
        print(somaMax)
    else:
        print(somaMax - 1)


if __name__ == "__main__":
    main()