import sys; sys.stdin = open('1219.txt', 'r')
# 일방 통행 -> 방향성 그래프


for tc in range(1, 10+1):
    # 테스트 케이스의 번호, 길의 총 개수
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))

    G = [[] for _ in range(100)]
    for i in range(0, E*2, 2):  # E 의 2배
        # i, i + 1
        u, v = arr[i], arr[i+1]
        G[u].append(v)          # 방향성 있는 그래프

    visited = [0] * 100
    # 시작점을 스택에 push
    v = 0
    S = [0]
    visited[0] = 1

    while S:
        for w in G[v]:
            if not visited[w]:
                S.append(v)
                visited[w] = 1
                v = w
                break
        else:
            v = S.pop()
    print(visited[99])
