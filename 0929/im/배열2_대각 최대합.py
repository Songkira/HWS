import sys; sys.stdin = open('배열2_대각 최대합.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [1, 1, -1, -1]
    dc = [1, -1, 1, -1]
    maxV = 0
    for r in range(N):
        for c in range(N):
            sumV = arr[r][c]
            for i in range(4):
                for j in range(1, N + 1):
                    nr = r + dr[i]*j
                    nc = c + dc[i]*j
                    if 0 <= nr < N and 0 <= nc < N:
                        sumV += arr[nr][nc]
                        if maxV < sumV:
                            maxV = sumV

    print(f'#{tc} {maxV}')


