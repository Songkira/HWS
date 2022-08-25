# 노드의 거리
import sys; sys.stdin = open('5102.txt', 'r')

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    # arr = list(map(int, input().split()))
    for _ in range(0, E):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    s, e = map(int, input().split())


    def BFS2(s):
        visit = [0] * (V + 1)
        Q = [s]
        visit[s] = 1  # 시작점을 방문하고, 큐에 삽입
        while Q:  # 빈 큐가 아닐동안 반복
            v = Q.pop(0)  # v의 방문하지 않은 인접 정점 w을 찾는다.
            for w in G[v]:
                if not visit[w]:
                    Q.append(w)
                    visit[w] = visit[v] + 1

        # s(출발)에서 g(도착) 까지의 거리 = visit[g] - 1
        print(visit[1:])


    BFS2(s)

    # print(f'#{tc} {bfs(sti, stj, N)}')
