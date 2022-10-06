dr = [-1 , 1, 0, 0]
dc = [0, 0, -1, 1]
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    for r in range(N):
        for c in range(M):
            if arr[r][c] == '#':
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
