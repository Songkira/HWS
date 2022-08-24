# solving club stack2_미로_확인용 D2
import sys; sys.stdin = open('미로2.txt', 'r')

# DFS 최단경로
# 모든 경로를 돌아봐야한다.=>'최단경로' 보다 '경로의 수'를 구하는게 더 빠르다?쉽다?
# 출발지에서 도달할수 있는 모든 칸은 몇개? 가능
# --------------------------------
# dfs(i, j, N) # 모든 칸을 돌아봐
#   if maze[i][j] == 3:
#       return
#   else:
#       visited[i][j] = 1
#       ni, nj = 계산해서
#       if visited == 0:
#           f(ni, nj, N)
# ----------------------------
# 중복 빠짐없이 도는 코드
#    f(i, N)
#       visited[v] = 1
#       for w in adjList[v]:
#           if visited[v] == 0:
#               f(w, N)

# DFS
# def dfs(i, j, N):
#     global answer
#     if maze[i][j] == 3:
#         answer += 1
#         return
#     else:
#         visited[i][j] = 1
#         for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#             ni, nj = i + di, j + dj
#             # 벽으로 둘러쌓인 미로
#             if maze[ni][nj]!=1 and visited[ni][nj]==0:
#                 dfs(ni, nj, N)
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
#     visited = [[0]*N for _ in range(N)]
#     dfs(sti, stj, N)
#     print(answer)
# 3번째 예시 의 경우 4개가 나와야 하는데 2개만 이라고 출력됨.
# '방문 안한곳이면 가라'(중복 허용 안됨) 설정되어 있어서 중복된 루트면 진행 중단.
# 그렇다고 방문 체크를 없애면 루트 무한 반복이 될수 있어서 코드 날리면 안됨.
# 다른 경로로 루트 진입하는 걸 허용하려면? 나로 돌아오는건 막고
# -------------------------------------------
# 3번째 예시 답이 4개가 출력되는 코드

# 가능한 모든 경로를 탐색하는(보는) 코드!!!!!!
#
def dfs(i, j, N):
    global answer
    if maze[i][j] == 3:
        answer += 1
        return
    else:
        visited[i][j] = 1 # 들어오면 일단 체크
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            # 벽으로 둘러쌓인 미로
            if maze[ni][nj]!=1 and visited[ni][nj]==0:
                dfs(ni, nj, N)
        # 리턴하기 전에 (visited[i][j] = 1 # 들어오면 일단 체크) 했던 걸 지우고
        # 내가 리턴을 할텐데 혹시 다른쪽 을 통해서 나를 들어오게 된다면 그땐 들어오게 해줄께
        visited[i][j] = 0
        return

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

    answer = 0             # 경로의 개수
    visited = [[0]*N for _ in range(N)]
    dfs(sti, stj, N)
    print(answer)

# -----------------------------------------