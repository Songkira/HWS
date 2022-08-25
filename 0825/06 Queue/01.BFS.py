import sys; sys.stdin = open('graph_input.txt', 'r')
# DFS와 BFS의 차이
# DFS 그래프가 어떻게 저장되어있느냐에 따라 다음지점이 달라짐
# 1 -> [2, 3]이면 2 부터, 1 -> [3, 2]이면 3부터
# 최단거리를 찾을땐 원래는 안되는데, 코드에 수정을하면 가능은 함.
# 한번 방문했던 곳은 가지 않기 때문
# 최단거리 찾을 땐 BFS

V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
arr = list(map(int, input().split()))
for i in range(0, E*2, 2):
    u, v = arr[i], arr[i + 1]
    G[u].append(v)
    G[v].append(u)

#=======================================
# def BFS1(s):  # s : 시작점
#     visited = [0] * (V + 1)   # 정점의 개수 (주의: 1부터인지 0부터인지 확인필요)
#     Q = [s]  # equeue => List.append(), dequeue => List.pop(0)
#     # 시작점을 방문표시하고 큐에 삽입
#     visited[s] = 1
#     while Q:            # 빈 큐가 아닐동안
#         v = Q.pop(0) # v --> w
#         print(v, end=' ')
#         print(visited)
#         for w in G[v]: # v에 방문하지 않은 인접정점들을 찾아서
#             if not visited[w]:
#                 visited[w] = 1
#                 Q.append(w)
#                 print(Q, end=' ')
#                 print(visited)
# BFS1(1)

#=======================================
def BFS1(s):           # 시작점
    visit = [0] * (V + 1)   # 정점의 개수 (주의: 1부터인지 0부터인지 확인필요)
    D = [0] * (V + 1)  # 시작점에서 각 정점까지의 최단 거리(정점의 개수만큼)
    P = [0] * (V + 1)  # 최단 경로 트리(부모 저장)
    Q = [s]
    D[s] = 0
    visit[s] = 1        # 시작점을 방문하고, 큐에 삽입
    while Q:            # 빈 큐가 아닐동안 반복
        v = Q.pop(0)
        for w in G[v]:  # v의 방문하지 않은 인접 정점 w을 찾는다.
            if not visit[w]:
                Q.append(w)
                visit[w] = 1;
                D[w] = D[v] + 1
                P[w] = v
    print(D[1:])

BFS1(1)
#
#
# #=========================================
# def BFS2(s):
#     visit = [0] * (V + 1)
#     Q = [s]
#     visit[s] = 1        # 시작점을 방문하고, 큐에 삽입
#     while Q:            # 빈 큐가 아닐동안 반복
#         v = Q.pop(0)    # v의 방문하지 않은 인접 정점 w을 찾는다.
#         for w in G[v]:
#             if not visit[w]:
#                 Q.append(w)
#                 visit[w] = visit[v] + 1
#
#     # s(출발)에서 g(도착) 까지의 거리 = visit[g] - 1
#     print(visit[1:])
#
# BFS2(1)



