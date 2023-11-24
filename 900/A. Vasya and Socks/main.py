def main():
    n, m = map(int, input().split())
    if n < m:
        print(n)
    else:
        m2 = m
        socks = n
        i = 0
        while socks > 0:
            socks -= 1
            i += 1
            if i == m2:
                socks += 1
                m2 += m
        print(i)


if __name__ == "__main__":
    main()