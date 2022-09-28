def prim2(r, V):
    MST = [0] * (V+1)       # MST 포함여부
    MST[r] = 1              # 시작정점 표시
    s = 0                   # MST간선의 가중치의 합
    for _ in range(V):
        u = 0
        minV = 10000
        for i in range(V+1):# MST에 포함된 정점i와 인접한 정점 j 중 MST에 포함된 지
            if MST[i] == 1:
                for j in range(V+1):
                    if adjM[i][j] > 0 and MST[j]==0 and minV>adjM[i][j]:
                        u = j
                        minV = adjM[i][j]
        s += minV
        MST[u] = 1
    return s


V, E = map(int, input().split())
adjM = [[0] * (V+1) for _ in range(V+1)]

for _ in range(E):
    u, v, w= map(int, input().split())
    adjM[u][v] = w
    adjM[v][u] = w      # 가중치가 있는 무방향 그래프

print(prim2(0,V))