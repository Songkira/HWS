
import sys; sys.stdin = open('배열2_폭격 작전.txt', 'r')

for tc in range(1, int(input())+1):
    N, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    sumV = 0
    for _ in range(C):
        r, c, l = map(int, input().split())
        sumV += arr[r][c]
        arr[r][c] = 0
        for i in range(4):
            for j in range(1, l+1):
                nr = r + dr[i]*j
                nc = c + dc[i]*j
                if 0 <= nr < N and 0 <= nc <N:
                    sumV += arr[nr][nc]
                    arr[nr][nc] = 0

    print(f'#{tc} {sumV}')