import sys; sys.stdin = open('5105.txt', 'r')
#
def bfs(i, j):
    visited = [[0]*N for _ in range(N)]
    q = []
    q.append((i, j))
    visited[i][j] = 1
    while q:
        r, c = q.pop(0)
        if maze[r][c] == 3: # 3번인가? == '도착지'인가?
            return visited[r][c] - 2
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != 1 and visited[nr][nc] == 0:
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si, sj = i, j
                break

    print(f'#{tc} {bfs(si, sj)}')  # 시작, 마지막 정점, 목표 정점 번호
#
# def start():
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == '2':
#                 return i, j
#     else:
#         return -1 -1
#
# def bfs(y, x):
#     queue = []
#     queue.append((y, x))
#     visited[y][x] = 1
#     while queue:
#         cy, cx = queue.pop(0)
#         if arr[cy][cx] == '3':
#             return visited[cy][cx] - 2
#         for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#             ny, nx = cy + dy, cx + dx
#             if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] != '1' and visited[ny][nx] == 0:
#                 visited[ny][nx] = visited[cy][cx] + 1
#                 queue.append((ny, nx))
#     return 0
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(input()) for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]
#     si, sj = start()
#     print('#{} {}'.format(tc, bfs(si, sj)))