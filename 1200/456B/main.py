def main():
    n = input()
    if int(n[-2:]) % 4 == 0:
        print(4)
    else:
        print(0)


if __name__ == "__main__":
    main()