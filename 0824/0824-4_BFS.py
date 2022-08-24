# A~G -> 0~6
# adjList = [[1, 2],    # 0
#            [0, 3, 4], # 1
#            [0, 4],    # 2
#            [1, 5],    # 3
#            [1, 2, 5], # 4
#            [3, 4, 6], # 5
#            [5]]       # 6

# 0번부터 V번까지, E개의 간선
# 6 8
# 0 1
# 0 2
# 1 3
# 1 4
# 2 4
# 3 5
# 4 5
# 5 6
# ---------------------------------------------
# 1. 탐색하는 순서만 찍어보기
def bfs(v, N):  # v 시작정점, N 마지막 정점 번호
    visited = [0]* (N+1)    # visited 생성
    q = []                  # queue 생성
    q.append(v)        # q = [v] <- 이 코드와 동일    # 시작점 인큐
    visited[v] = 1          # 시작점 처리 표시
    while q:                # queue가 비어있지 않으면
        v = q.pop(0)         # q가 비어있지 않으면 dequeue
        print(v)                # visited(v)
        for w in adjList[v]:    # 인접하고 미방문(인큐되지 않은) 정점 w가 있으면
            if visited[w] == 0: #
                q.append(w)
                visited[w] = visited[v] +1

V, E = map(int, input().split())
N = V + 1           # N 정점 개수
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

bfs(0, V)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# ---------------------------------------------
'''6 8
0 2
0 1
3 1
1 4
2 4
5 3
4 5
6 5'''
# 1. 탐색하는 순서만 찍어보기

def bfs(v, N):  # v 시작정점, N 마지막 정점 번호
    visited = [0]* (N+1)    # visited 생성
    q = []                  # queue 생성
    q.append(v)        # q = [v] <- 이 코드와 동일    # 시작점 인큐
    visited[v] = 1          # 시작점 처리 표시
    while q:                # queue가 비어있지 않으면
        v = q.pop(0)         # q가 비어있지 않으면 dequeue
        print(v)                # visited(v)
        for w in adjList[v]:    # 인접하고 미방문(인큐되지 않은) 정점 w가 있으면
            if visited[w] == 0: #
                q.append(w)
                visited[w] = visited[v] +1

V, E = map(int, input().split())
N = V + 1           # N 정점 개수
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

bfs(0, V)
# 0
# 2
# 1
# 4
# 3
# 5
# 6
# ---------------------------------------------


# ---------------------------------------------

# ---------------------------------------------

# ---------------------------------------------


# ---------------------------------------------
