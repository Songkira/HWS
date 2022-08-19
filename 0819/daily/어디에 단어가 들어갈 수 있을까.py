import sys; sys.stdin = open('어디에 단어가 들어갈 수 있을까.txt', 'r')

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        row_key = 0
        for j in range(N):
            if arr[i][j] == 1:
                row_key += 1
                if row_key == K:
                    cnt += 1
                if row_key > K:
                    cnt -= 1
                    row_key = 0
            if arr[i][j] == 0:
                row_key = 0

    for j in range(N):
        ver_key = 0
        for i in range(N):
            if arr[i][j] == 1 :
                ver_key += 1
                if ver_key == K:
                    cnt += 1
                if ver_key > K:
                    cnt -= 1
                    ver_key = 0
            if arr[i][j] == 0:
                ver_key = 0
    print(f'#{tc}', cnt)
