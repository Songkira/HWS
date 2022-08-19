import sys; sys.stdin = open('1219.txt', 'r')

A = 0
B = 99
for _ in range(1, 11):
    case, E = map(int, input().split())  # T:테스트 케이스, E:간선 개수

    G = [[] for _ in range(100)]  # 간선
    gList = list(map(int, input().split()))
    for i in range(0, E * 2, 2):
        G[gList[i]].append(gList[i + 1])  # 각 정점에서 갈 수 있는 정점 저장

    visited = [0 for _ in range(100)]  # 방문 여부
    visited[A] = 1  # 시작 정점 방문


    def dfs(A, B):  # DFS
        for w in G[A]:  # 현재 정점에서 갈 수 있는 다른 정점 확인
            if visited[w] == 0:  # 방문한 적이 없으면
                visited[w] = 1  # 방문
                if w == B:  # 해당 정점이 목표 정점이면 종료
                    return
                dfs(w, B)  # 연결된 정점으로 이동


    dfs(A, B)
    print(f'#{case} {visited[B]}')