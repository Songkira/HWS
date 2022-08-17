# 재귀
def dfs(v):
    print(v)    # v 방문
    visited[v] = 1
    for w in adjList[v]:
        if visited[w] == 0:         # 방문하지 않은 w
            dfs(w)

V, E = map(int, input().split())
N = V + 1
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)            # append 작업 들을 해야
    adjList[b].append(a)            # 서로 연결됨

visited = [0] * N
dfs(0)