import sys; sys.stdin = open('미로.txt', 'r')

def bfs(i, j, N):
    visited = [[0]*N for _ in range(N)]
    q = []
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        if maze[i][j] == 3: # 3번인가? == '도착지'인가?
            return 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0

# T = int(input())
for i in range(1, 10+1):
    tc = int(input())
    N = 16
    maze = [list(map(int, input())) for _ in range(N)]

    sti = -1 # 0 으로 설정하면 (0, 0)이 존재하므로 혹시나 상황을 대비해서
    stj = -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j
                break # 여기서의 break 인덱스 j for 문이 중단됨.
        if sti != -1: # 여기는 인덱스 i의 for문
            break # (2:시작점)을 찾으면 쓸데없이 더 돌지 말라고 중단 시킴

    print(f'#{tc} {bfs(sti, stj, N)}')