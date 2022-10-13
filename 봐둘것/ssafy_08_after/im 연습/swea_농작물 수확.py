# import sys; sys.stdin = open('농작물 수확.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    minV = 99999999999
    for i in range(N-1):
        for j in range(N-1):
            sumin = kira = hyounsuk = 0
            for r in range(0, i + 1):
                for c in range(0, j + 1):
                    if c < N - 1 and r < N -1:
                        sumin += arr[r][c]
            for r in range(i+1, N):
                for c in range(0, j + 1):
                    if c < N - 1:
                        kira += arr[r][c]
            for r in range(N):
                for c in range(j+1, N):
                    hyounsuk += arr[r][c]

            if minV > max(sumin, kira, hyounsuk) - min(sumin, kira, hyounsuk):
                minV = max(sumin, kira, hyounsuk) - min(sumin, kira, hyounsuk)

    print(f'#{tc} {minV}')
