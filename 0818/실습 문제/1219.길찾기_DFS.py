import sys; sys.stdin = open('1219.txt', 'r')

for tc in range(1, 10+1):
    # 테스트 케이스의 번호, 길의 총 개수
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)

    for _ in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
    for i in range(1, V + 1):
        print(i, '-->', G[i])

    s, e = 0, 99

    def dfs(v):  # v: 현재 방문할 정점 번호
        # 정점을 방문한다.
        visited[v] = 1;  # print(f'v: {v}',end=' ')
        # v 의 방문하지 않은 정점들을 조사한다.
        for w in G[v]:  # v의 인접 정점을 w를 찾는다.
            if visited[w] == 0:
                dfs(w)
    dfs(s)
    if visited[e] == 1:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)