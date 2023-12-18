import math


def distance(x1, x2):
    dist = 0
    for i in range(0, i):
        dist += (x1[i] - x2[i])**2
    return math.sqrt(dist)


def main():
    t = int(input())
    for _ in range(0, t):
        P = list(map(int, input().split()))     # house location
        A = list(map(int, input().split()))     # lantern 1
        B = list(map(int, input().split()))     # lantern 2

        distP, distA, distB = distance([0, 0], P), distance([0, 0], A), distance([0, 0], B)
        minR = min(distA, distB)
        maxR = minR + distP
        

        distPA, distPB = distance(P, A), distance(P, B)


if __name__ == "__main__":
    main()