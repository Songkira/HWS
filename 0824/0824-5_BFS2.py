import sys; sys.stdin = open('input.txt', 'r')
# stack1_실습 문제 / 1219. [S/W 문제해결 기본] 4일차 - 길찾기 D4
# def bfs(v, N, t): # v 시작, N 마지막 정점(번호), t 찾는 정점
#     visited = [0] * (N+1)
#     q = []
#     q.append(v)
#     visited[v] = 1
#     while q:
#         v = q.pop(0)
#         if v == t:      # visit(v)
#             return 1      # 목표 발견
#         for w in adjList[v]: # v 에 인접하고 방문안한 w enQueue, 표시
#             if visited[w] == 0:
#                 q.append(w)
#                 visited[w] = visited[v] + 1
#     return 0
#
# T = 10
# for _ in range(T):
#     tc, E = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     adjList = [[] for _ in range(100)]
#     for i in range(E):
#         a, b = arr[i*2], arr[i*2 + 1]
#         adjList[a].append(b)            # 단방향
#
#     # print(adjList)
#     print(f'#{tc} {bfs(0, 99, 99)}')  # 시작, 마지막 정점, 목표 정점 번호
#1 1
#2 1
#3 1
#4 0
#5 1
#6 1
#7 0
#8 0
#9 0
#10 0
#============================================
# 99번 까지 도착하는데 몇개를 지나왔니? visited안에 들어있음
def bfs(v, N, t): # v 시작, N 마지막 정점(번호), t 찾는 정점
    visited = [0] * (N+1)
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        if v == t:      # visit(v)
            return visited[99]      # 목표 발견
        for w in adjList[v]: # v 에 인접하고 방문안한 w enQueue, 표시
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1
    return 0

T = 10
for _ in range(T):
    tc, E = map(int, input().split())
    arr = list(map(int, input().split()))

    adjList = [[] for _ in range(100)]
    for i in range(E):
        a, b = arr[i*2], arr[i*2 + 1]
        adjList[a].append(b)            # 단방향

    # print(adjList)
    print(f'#{tc} {bfs(0, 99, 99)}')  # 시작, 마지막 정점, 목표 정점 번호
#1 5
#2 14
#3 13
#4 0
#5 14
#6 14
#7 0
#8 0
#9 0
#10 0
# ----------------------------------------------
