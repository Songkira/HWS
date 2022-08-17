# A~G -> 0~6
# adjList = [[1, 2],      # 0
#            [0, 3, 4],   # 1
#            [0, 4],      # 2
#            [1, 5],      # 3
#            [1, 2, 5],   # 4
#            [3, 4, 6],   # 5
#            [5]]         # 6

def dfs(v, N):

    top = -1
    print(v)            # 방문
    visited[v] = 1      # 시작점 방문 표시
    while True:
        for w in adjList[v]:        # if ( v의 인접 정점 중 방문 안 한 정점 w가 있으면)
            if visited[w] == 0:
                top += 1            #push(v);
                stack[top] = v
                v = w               # v  w;  (w에 방문)
                print(v)  # 방문
                visited[w] = 1      # visited[w] true;
                break
        else:                       # w가 없으면
            if top != -1:           # 스택이 비어있지 않은 경우
                v = stack[top]          # pop
                top -= 1
            else:                   # 스택이 비어있으면
                break               # while

V, E = map(int, input().split())
N = V + 1
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

visited = [0] * N   # visited 생성
stack = [0] * N     # stack 생성
dfs(1, N)
print()

#=======================================================
def dfs(v):
    print(v)    #  v 방문
    visited[v] = 1
    for w in adjList[v]:
        if visited[w] == 0:     # 방문하지 않은 w
            dfs(w)

V, E = map(int, input().split())
N = V + 1
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

visited = [0] * N   # visited 생성
dfs(0)