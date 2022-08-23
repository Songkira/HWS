import sys; sys.stdin = open('4875.txt', 'r')
#1 1
#2 1
#3 0
# 미로
def dfs(r, c):
    visited[r][c] = 1
    if r == er and c == ec: # 중간에 끊고 싶으면
        return 1

    for i in range(4):
        # (r, c)의 상하좌우 인접한 곳의 좌표를 생성
        nr, nc = r + dr[i], c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= N:  # 경계체크
            continue
        # 목적지는 3이기 때문에 0으로만 가면 절대로 도착 못함
        # 길이거나 방문안했으면
        if maze[nr][nc] != 1 and visited[nr][nc] == 0:
            dfs(nr, nc)

for tc in range(1, int(input())+1):
    # 하상우좌
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]


    visited = [[0] * N for _ in range(N)]  # 지나온 길을 기록할 맵
    S = []
    # 시작점을 찾는다
    r = c = er = ec = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                r, c = i, j
            elif maze[i][j] == 3:
                er, ec = i, j


    dfs(r, c)
    print(f'#{tc}', visited[er][ec])
