T = int(input())

for test in range(T):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    r = c = 0
    loc = 0

    # 달팽이=>우하좌상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    for i in range(1, N*N+1):
        arr[r][c] = i

        r = r + dr[loc]
        c += dc[loc]

        if r < 0 or c < 0 or r >= N or c >= N or arr[r][c] != []:
            r -= dr[loc]
            c -= dc[loc]

            loc = (loc+1) % 4

            r += dr[loc]
            c += dc[loc]

    for line in arr:
        print(*line)




