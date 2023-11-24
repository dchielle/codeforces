def main():
    t = int(input())
    for _ in range(0, t):
        n = int(input())
        if n < 2020:
            print("NO")
        elif n % 2020 == 0 or n % 2021 == 0:
            print("YES")
        else:
            skip = 1
            k = n % 10
            q = int(n / 2021)
            while k <= q:
                m = n - k * 2021
                if m % 2020 == 0:
                    print("YES")
                    skip = 0
                k += 10

            if skip:
                print("NO")



if __name__ == "__main__":
    main()