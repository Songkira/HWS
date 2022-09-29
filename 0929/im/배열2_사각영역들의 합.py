import sys; sys.stdin = open('배열2_사각영역들의 합.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    num = 0
    for _ in range(M):
        r, c, l = map(int, input().split())
        num += arr[r][c]
        arr[r][c] = 0
        for i in range(l):
            for j in range(l):
                if 0 <= r + i < N and 0 <= c + j < N:
                    num += arr[r+i][c+j]
                    arr[r+i][c+j] = 0


    print(f'#{tc} {num}')
