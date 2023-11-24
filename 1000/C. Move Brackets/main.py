def main():
    t = int(input())
    for _ in range(0, t):
        n = int(input())
        s = list(input())

        countOpen = 0
        countClose = 0
        moves = 0
        for i in range(0, n):
            if s[i] == ')':
                countClose += 1
            else:
                countOpen += 1

            if countClose > countOpen:
                moves += 1
                countClose -= 1

        print(moves)


if __name__ == "__main__":
    main()