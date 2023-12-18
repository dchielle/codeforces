def lucky_checker(s):
    count = 0
    for char in s:
        if char == '4' or char == '7':
            count += 1
    return count


def main():
    n = input()
    m = str(lucky_checker(n))
    o = lucky_checker(m)

    if o == len(m):
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    main()