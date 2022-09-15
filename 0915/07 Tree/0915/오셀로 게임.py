import sys; sys.stdin = open('오셀로게임.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = int(input().split())
    arr = [[0] * N for _ in range(N)]

    for _ in range(M):
        a, b, x = map(int, input().split())
        a, b = a-1, b-1
        arr[a][b] = x
        if a-1 >= 0 and a + 1 < N:
            if arr[a-1] == arr[N-1] == 2:
                arr[a-1:N-1] = 2


