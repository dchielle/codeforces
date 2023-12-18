def main():
    n = int(input())
    score = {}
    for i in range(0, n):
        t = input()
        if t in score:
            score[t] += 1
        else:
            score[t] = 1

    print(max(score, key = score.get))


if __name__ == "__main__":
    main()