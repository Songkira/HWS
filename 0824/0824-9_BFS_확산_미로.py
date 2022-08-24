import sys; sys.stdin = open('미로3.txt', 'r')
# 2 를 시작점으로 두고 위,아래,좌,우 로 한칸씩 바이러스가 전염된다고 할때
# 칸 전부 '확산(전염)'되는 횟수는?
# 제일 큰 숫자 찾으면 됨.
# 내가 실습해보기 지금 값은 None으로 나옴.

def bfs(N):
    visited = [[0]*N for _ in range(N)]
    q = []
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                q.append((i, j))
                visited[i][j] = 1
    while q:
        i, j = q.pop(0)

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    print(f'#{tc} {bfs(N)}')