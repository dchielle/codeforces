def main():
    n, m = map(int, input().split())
    words = [[0]*m, [1]*m]
    aORb = [0]*m
    for i in range(0, m):
        words[0][i], words[1][i] = input().split()
        if len(words[1][i]) < len(words[0][i]):
            aORb[i] = 1

    inputText = input().split()
    outputText = ''
    for i in range(0, n):
        index = words[0].index(inputText[i])
        outputText += words[aORb[index]][index]
        if i < n - 1:
            outputText += ' '

    print(outputText)


if __name__ == "__main__":
    main()