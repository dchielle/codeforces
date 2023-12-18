def build_divisors(digits):
    l = [4, 7]
    if digits >= 2:
        for i in range(0, len(l)):
            l.append(l[i] * 10 + 4)
            l.append(l[i] * 10 + 7)

    if digits >= 3:
        for i in range(0, len(l)):
            l.append(l[i] * 10 + 4)
            l.append(l[i] * 10 + 7)

    return l


def main():
    n = input()
    digits = len(n)
    n = int(n)
    divisors = build_divisors(digits)

    for item in divisors:
        if n % item == 0:
            print('YES')
            return

    print('NO')


if __name__ == "__main__":
    main()