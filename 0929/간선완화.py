for tc in range(int(input())):
    N, E = map(int, input().split())
    # 정점 0번 ~ N번까지
    G = [[] for _ in range(N+1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        G[u].append((v,w))

    D = [0xffffff] *(N+1)       # 거리를 저장하는 배열, 방문정보는 필요없음
    D[0] = 0                    # 출발점을 0으로 초기화!! 무조건
    q = [0]

    # BFS
    while q:
        u = q.pop(0)
        for v, w in G[u]:
            # (u,v) 간선 완화
            if D[v] > D[u] + w:
                D[v] = D[u] + w
                q.append(v)

    # # DFS
    # def dfs(u):
    #     for v, w in G[u]:
    #         if D[v] > D[u] + w:
    #             D[v] =D[u] + w
    #             dfs(v)
    # dfs(0)

    # # 완전탐색
    # while True:
    #     flag = False
    #     for u in range(N):
    #         for v, w in G[u]:
    #             if D[v] > D[u] + w:
    #                 flag = True
    #                 D[v] =D[u] + w
    #     if flag:
    #         break
    print(f'#{tc+1}', D[N])