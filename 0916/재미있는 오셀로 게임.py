import sys; sys.stdin = open('오셀로.txt', 'r')
# 상좌하우
dr = [-1, 0, 1, 0, -1, 1, 1, -1]
dc = [0, -1, 0, 1, -1, -1, 1, 1]

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    # 흑 = 1, 백 = 2
    arr[N//2][N//2] = 2
    arr[N//2-1][N//2-1] = 2
    arr[N//2-1][N//2] = 1
    arr[N//2][N//2-1] = 1

    for _ in range(M):
        r, c, color = map(int, input().split())
        r, c = r - 1, c - 1
        arr[r][c] = color

        for i in range(8):
            lst = []
            for j in range(1, N+1):
                nr = r + dr[i] * j
                nc = c + dc[i] * j

                if 0 <= nr < N and 0 <= nc < N:
                    # 0인 경우는 배제
                    if arr[nr][nc] == 1 or arr[nr][nc] == 2:
                        if arr[nr][nc] != arr[r][c]:
                            lst.append([nr, nc])
                        else:
                            if lst:
                                for k, l in lst:
                                    arr[k][l] = arr[r][c]
                            break
                    else:
                        break
                            #         for n in arr:
                            #             print(*n)
                            # print('----------')

    black = white = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                black += 1
            elif arr[i][j] == 2:
                white += 1

    print(f'#{tc}', black, white)
