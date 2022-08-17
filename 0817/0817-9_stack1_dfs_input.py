'''
0번부터 N번까지, E개의 간선
- 빠른 번호가 먼저 들어온다는 보장 없음
- 겹치는 건 제외하고
6 8
0 1
0 2
1 3
1 4
2 4
3 5
4 5
5 6
'''

def dfs(v, N):

    top = -1
    print(v)

    visited[v] = 1      # 시작점 방문 표시
    while True:
        # 어느곳을 방문 안했는지 모르니 순서대로 꺼내보기
        for w in adjList[v]:        # if ( v의 인접 정점 중 방문 안 한 정점 w 가 있으면)
            if visited[w] == 0:     # [false]로 표시한 분들은 0 대신 false 써도 됨
                top += 1            # push(v);
                stack[top] = v
                v = w                # v <- w; (w에 방문)
                print(v)            # 방문
                visited[w] = 1      # visited[w] <- true;
                break
        else:                       # w가 없으면
            if top != -1:           # 스택이 비어있지 않은 경우
                v = stack[top]      # pop
                top -= 1
            else:                   # 스택이 비어있으면
                break               # while 을 빠져나오게 함.

V, E = map(int, input().split())
N = V + 1
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)            # append 작업 들을 해야
    adjList[b].append(a)            # 서로 연결됨

visited = [0] * N   # visited 생성 /visited = [1, 1, 1, 1, 1, 1, 1]
stack = [0] * N     # stack생성 / stack = [1, 0, 2, 4, 5, 0, 0]
dfs(1, N)
print()