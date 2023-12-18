import math


def main():
    t = int(input())
    for _ in range(0, t):
        n = int(input())
        k = int(math.log(n) / math.log(2)) + 1
        for i in range(2, k+1):
            x = n/(2**i - 1)
            if x % 1 == 0:
                print(int(x))
                break


if __name__ == "__main__":
    main()