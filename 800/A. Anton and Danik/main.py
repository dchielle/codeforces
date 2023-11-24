def main():
    n = int(input())
    s = input()

    d = 0

    for char in s:
        if char == 'D':
            d += 1

    v = d/n

    if v > .5:
        print("Danik")
    elif v < .5:
        print("Anton")
    else:
        print("Friendship")


if __name__ == "__main__":
    main()