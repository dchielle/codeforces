def main():
    side = input()
    text = input()

    keyboard = list('qwertyuiopasdfghjkl;zxcvbnm,./')
    if side == 'R':
        k = -1
    else:
        k = 1

    fixedText = ''
    for char in text:
        fixedText += keyboard[keyboard.index(char) + k]

    print(fixedText)


if __name__ == "__main__":
    main()