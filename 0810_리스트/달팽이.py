T = int(input())

for test in range(T):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    r = c = 0
    loc = 0

    # 우, 하, 좌, 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    for i in range(1, N*N +1):
        arr[r][c] = i
        r += dr[loc]
        c += dr[loc]

        if r < 0 or c < 0 or r == N or c == N or arr[r][c] != []:
            r -= dr[loc]
            c -= dr[loc]

            loc = (loc + 1) % 4

            r += dr[loc]
            c += dr[loc]
    print(f'#{test+1}')
    for line in arr:
        print(*line)
    print()

