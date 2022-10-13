T = int(input())

for _ in range(T):
    # 용량, 지점의 개수
    W, N = map(int, input().split())

    lst = []
    for _ in range(N):
        [x_i, w_i] = map(int, input().split())
        lst.append([x_i, w_i])

    weight = length = 0
    for i in range(N):
        weight += lst[i][1]
        length += lst[i][0]
        if weight >= W:
            weight = 0

