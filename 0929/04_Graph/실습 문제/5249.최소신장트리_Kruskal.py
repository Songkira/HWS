import sys; sys.stdin = open('5249.txt', 'r')


for tc in range(1, int(input())+1):
    # 간선정보 그대로 저장
    N, E = map(int, input().split())
    # 간선들의 리스트[[u, v, weight], [], [], []]
    edges = [list(map(int, input().split())) for _ in range(E)]

    # 간선들 저장
    # kruskal 알고리즘
    # 1. 간선들의 가중치 오름차순으로 정렬
    edges.sort(key=lambda x: x[2], reverse=True)    # 내림차순

    # Disjoin-set 준비
    p = [i for i in range(N + 1)]   # 정점 0번 ~ N번까지 make-set()
    def find_set(x):        # 반복
        while x != p[x]:    # 루트인지 아닌지 확인
            x = p[x]
        return x
    # =====================================================
    mst = []    # MST 간선들
    ans = 0     # 간선들 가중치 합

    # 정점 수 = N + 1 개 이므로 MST의 간선수는 N 개
    cnt = N
    while cnt:
        u, v, weight = edges.pop()
        a = find_set(u)
        b = find_set(v)
        if a == b:          # 싸이클이 생기는 간선은 skip
            continue
        ans += weight
        # mst.append([u, v, weight])
        p[a] = b        # union(a, b) 또는 p[b] = a
        cnt -= 1

    print(f'#{tc} {ans}')
