def main():
    n = int(input())
    digits = "8426"
    if n == 0:
        print("1")
    else:
        print(digits[n % 4 - 1])


if __name__ == "__main__":
    main()