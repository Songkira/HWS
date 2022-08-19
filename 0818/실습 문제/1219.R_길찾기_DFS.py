import sys; sys.stdin = open('1219.txt', 'r')

for tc in range(1):
    # 테스트 케이스의 번호, 길의 총 개수
    N, E = map(int, input().split())

    G = [[] for _ in range(100)]
    visited = [0] * 100
    lst = list(map(int, input().split()))

    for i in range(0, E*2, 2):
        G[lst[i]].append(lst[i+1])
        # G[v].append(u)
    for i in range(1, 100):
        print(i, '-->', G[i])

    s, e = 0, 99

    def dfs(v1, v2):  # v: 현재 방문할 정점 번호
        # 정점을 방문한다.
        visited[v1] = 1  # print(f'v: {v}',end=' ')
        # v 의 방문하지 않은 정점들을 조사한다.
        for w in G[v1]:  # v의 인접 정점을 w를 찾는다.
            if visited[w] == 0:
                # visited[w] = 1
                # if w == v2:
                #     return
                dfs(w, v2)
    dfs(s, e)
    print(f'#{N} {visited[e]}')