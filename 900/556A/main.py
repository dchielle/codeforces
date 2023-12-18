def main():
    n = int(input())
    s = input()
    size = n
    ones = []
    zeros = []
    k = 0
    for i in range(0, n):
        if s[i] == '0':
            zeros.append(i - k)
        else:
            ones.append(i - k)

        while len(ones)*len(zeros) > 0 and abs(ones[-1] - zeros[-1]) == 1:
            size -= 2
            ones.pop()
            zeros.pop()
            k += 2

    print(size)


if __name__ == "__main__":
    main()