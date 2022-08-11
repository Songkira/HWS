import sys; sys.stdin = open("4836.txt", "r")
T = int(input())

for tc in range(T):
    N = int(input())
    arr = [[0]*10 for _ in range(10)]

    cnt = 0
    for i in range(N):
        color = list(map(int, input().split()))
        r1 = color[0]
        c1 = color[1]
        r2 = color[2]
        c2 = color[3]

        for r in range(r1, r2 + 1): # (2, 5)
            for c in range(c1, c2 + 1): # (2, 5)
                arr[r][c] += color[-1]

                if arr[r][c] == 3:
                    cnt += 1


    for line in arr:
        print(*line)

    print(f'#{tc+1} {cnt}')