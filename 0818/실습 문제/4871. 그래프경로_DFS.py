import sys; sys.stdin = open('4871.txt', 'r')

for tc in range(1, int(input())+1):
    # V = 정점의 갯수, E = 간선의 갯수
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)

    for _ in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
        # G[v].append(u)
    for i in range(1, V + 1):
        print(i, '-->', G[i])
    # 정점들의 방문정보를 저장할 공간이 필요
    s, e = map(int, input().split())

    def dfs(v):  # v: 현재 방문할 정점 번호
        # 정점을 방문한다.
        visited[v] = 1;  # print(f'v: {v}',end=' ')
        # v 의 방문하지 않은 정점들을 조사한다.
        for w in G[v]:  # v의 인접 정점을 w를 찾는다.
            if visited[w] == 0:
                dfs(w);  # print(f'w: {w}', end=' ')

    dfs(s) # 시작점을 인자로 함수 호출
    # print(visited)
    if visited[e] == 1:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)
