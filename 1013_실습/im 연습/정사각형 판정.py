import sys; sys.stdin=open('정사각형 판정.txt', 'r')
import time
import math

for tc in range(1, int(input())+1):
    # start = time.time()
    # math.factorial(100000)
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    ans = 'no'
    lst = []
    # lst_l = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '#':
                lst.append([i, j])
    maxV = 0
    for r, c in lst:
        if maxV < r:
            maxV = r
        if maxV < c:
            maxV = c

    base = N - maxV + 1
    # print(base)
    r, c = lst[0][0], lst[0][1]
    cnt = 0
    for a in range(r, r+base):
        for b in range(c, c+base):
            if arr[a][b] == '#':
                cnt += 1
                if cnt == base*base:
                    ans = 'yes'

# # 좌상단 구하고 1씩 늘려서 인덱스 확인?
#     M = 1
#     for _ in range(N):
#         i, j = lst[0][0], lst[0][1]
#         cnt = 0
#         for r in range(i, i+M):
#             for c in range(j, j+M):
#                 if 0 <= r < N and 0 <= c < N:
#                     if arr[r][c] == '#':
#                         cnt += 1
#                         if cnt != M*M:
#                             ans = 'no'
#                             break
#         M += 1

    # end = time.time()
    # print(f"{end - start:.5f} sec")
    # print(f'#{tc} {ans}')

    if len(lst) == 1:
        print(f'#{tc} {ans}')
    else:
        print(f'#{tc} {ans}')