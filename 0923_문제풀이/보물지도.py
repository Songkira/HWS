from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    Q = deque()
    Q.append((r, c))
    visited = [[0] * M for _ in range(N)]
    visited[r][c] = 1
    cnt = 0
    while Q:
        r, c = Q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 'L' and visited[nr][nc] == 0:
                    visited[nr][nc] = visited[r][c] + 1
                    cnt = max(cnt, visited[nr][nc])
                    Q.append((nr, nc))
                # for v in visited:
                #     print(*v)
                # print('# --------')
    return cnt-1


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            result = max(result, bfs(i, j))
print(result)