def create_string(n, a, b):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = ""
    for i in range(0, n):
        s += alphabet[i % b]

    return s


def main():
    t = int(input())
    for test in range(0, t):
        n, a, b = map(int, input().split())
        s = create_string(n, a, b)
        print(s)


if __name__ == "__main__":
    main()