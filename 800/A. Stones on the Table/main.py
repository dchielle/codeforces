def main():
    n = int(input())
    s = input()

    previous = ""
    count = 0
    for char in s:
        if char == previous:
            count += 1
        previous = char

    print(count)


if __name__ == "__main__":
    main()