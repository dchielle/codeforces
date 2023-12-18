import math


def main():
    n, x = map(int, input().split())
    md = int(math.sqrt(x)) + 1

    divisors = []
    if x <= n:
        divisors.append(1)
        if x != 1:
            divisors.append(x)

    for i in range(2, min(n, x // 2) + 1):
        rest = x % i
        q = x // i
        if rest == 0 and q <= n:
            divisors.append(i)

    print(len(divisors))


if __name__ == "__main__":
    main()