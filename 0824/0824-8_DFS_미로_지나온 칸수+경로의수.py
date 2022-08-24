# solving club stack2_미로_확인용 D2
import sys; sys.stdin = open('미로2.txt', 'r')

# 내가 거쳐간 칸 수를 세는 코드
# 내가 이전까지 지나온 칸 수를 알고있다면 di, dj 활용
# 출발지2, 도착지 3은 칸 수에서 제외해야함

# def dfs(i, j, s, N): # s = 지나온 칸 수
#     global minV
#     if maze[i][j] == 3:
#         if minV > s + 1:
#             minV = s + 1 # 일단 이 코드는 출발지, 도착지 포함
#         return
#     else:
#         visited[i][j] = 1 # 들어오면 일단 체크
#         for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#             ni, nj = i + di, j + dj
#             # 벽으로 둘러쌓인 미로
#             if maze[ni][nj]!=1 and visited[ni][nj]==0:
#                 dfs(ni, nj, s+1, N)
#         visited[i][j] = 0
#         return
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     maze = [list(map(int, input())) for _ in range(N)]
#
#     sti = -1
#     stj = -1
#     for i in range(N):
#         for j in range(N):
#             if maze[i][j] == 2:
#                 sti, stj = i, j
#                 break
#         if sti != -1:
#             break
#
#     answer = 0             # 경로의 개수
#     minV = N*N
#     visited = [[0]*N for _ in range(N)]
#     dfs(sti, stj, 0, N)
#     print(minV)
#     # 3
#     # 25 # 도착못했는데?? 초기화된 값이 그대로 들어갔음
#     # 13

# --------------------------------------------
# # 도착지에 못도착하는 맵 리턴값 수정
#
# def dfs(i, j, s, N): # s = 지나온 칸 수
#     global minV
#     if maze[i][j] == 3: # 도착지인가??
#         if minV > s + 1:
#             minV = s + 1 # 일단 이 코드는 출발지, 도착지 포함
#         return
#     else:
#         visited[i][j] = 1 # 들어오면 일단 체크
#         for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#             ni, nj = i + di, j + dj
#             # 벽으로 둘러쌓인 미로
#             if maze[ni][nj]!=1 and visited[ni][nj]==0:
#                 dfs(ni, nj, s+1, N)
#         visited[i][j] = 0
#         return
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     maze = [list(map(int, input())) for _ in range(N)]
#
#     sti = -1
#     stj = -1
#     for i in range(N):
#         for j in range(N):
#             if maze[i][j] == 2:
#                 sti, stj = i, j
#                 break
#         if sti != -1:
#             break
#
#     answer = 0             # 경로의 개수
#     minV = N*N
#     visited = [[0]*N for _ in range(N)]
#     dfs(sti, stj, 0, N)
#     if minV == N*N:
#         minV = -1
#     print(minV)
#     # 3
    # -1
    # 13
# ------------------------------------------------
# 0824-6 코드를 return 살짝 수정하면 같은 값 나옴
# 이건 BFS 코드 가져온거

def bfs(i, j, N):
    visited = [[0]*N for _ in range(N)]
    q = []
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        if maze[i][j] == 3: # 3번인가? == '도착지'인가?
            return visited[i][j]
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return -1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    sti = -1
    stj = -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j
                break
        if sti != -1:
            break

    print(f'#{tc} {bfs(sti, stj, N)}')
    # 1 3
    # 2 -1
    # 3 13