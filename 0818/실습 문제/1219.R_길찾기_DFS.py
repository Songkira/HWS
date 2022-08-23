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
#----------------------------------------------------------

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
#----------------------------------------------------------
# 1 ~ 98
# 시작점 0, 도착점 99
# V(정점)은 100개

for _ in range(1,11):
    tc, E = map(int,input().split())
    arr = list(map(int,input().split()))  # 정점->정점 정보 / 정점 간선정보로 나눠야함
    G = [[] for _ in range(100)]

    for i in range(0, E * 2, 2):
        u, v = arr[i], arr[i + 1]  # u ==> v / u = 출발, v = 도착 / 간선정보
        G[u].append(v)  # 간선정보 저장

    visited = [0] * 100

    v = 0  # 시작점
    visited[0] = 1  # 시작점 방문
    S = [v]  # 스택에 푸시

    while S:
        for w in G[v]:  # v의 인접정점 찾기
            if visited[w] == 0:
                S.append(v)  # 지나온 정점 v를 스택에 넣고
                visited[w] = 1
                v = w  # 방문점이 시작점이된다
                break
        else:
            v = S.pop()
    print(visited[99])

# ------------------------------------------------------------------------
# 재귀
def dfs(v):
    visited[v] = 1
    if v == 99:
        return 1
    for w in G[v]:
        if visited[w] == 0:
            dfs(w)
            return 1
    return 0

for _ in range(1,11):
    tc, E = map(int, input().split())  # tc 와 간선(E) 갯수
    arr = list(map(int,input().split()))  # 배열 받기
    G = [[] for _ in range(100)]  # 정점의 갯수대로 만들어 놓기

    # 간선 저장 리스트
    for i in range(0, E * 2, 2):
        u, v = arr[i], arr[i + 1]  # u ==> v / u = 출발, v = 도착 / 간선정보
        G[u].append(v)  # 간선정보 저장

    visited = [0] * 100
    dfs(0)
    if visited[99] == 1:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)