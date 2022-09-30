import sys; sys.stdin = open('요리사.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if r != c:
                Aval = arr[r][c] + arr[c][r]


    # print(Aval, Bval)