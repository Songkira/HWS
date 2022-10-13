import sys; sys.stdin = open('러시아 국기 같은 깃발.txt', 'r')

for tc in range(1, int(input())+1):
    # N개의 줄 == 행, M개의 문자로 이루어진 문자열 == 열
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    # 새로 칠해야 하는 칸의 개수의 최소값 구하기
    wcnt = 0
    lst = []
    for i in range(N-2):
        # wcnt += M
        wcnt += arr[i].count('W')
        bcnt = 0
        for j in range(i+1, N-1):
            # bcnt += M
            bcnt += arr[j].count('B')
            rcnt = 0
            for k in range(j+1, N):
                # rcnt += M
                rcnt += arr[k].count('R')

            lst.append([wcnt, bcnt, rcnt])
        # wcnt = bcnt = rcnt = 0
    # print(lst)
    # minV = 9999999
    # for val in lst:
    #     if minV > sum(val):
    #         minV = sum(val)
    # print(minV)
    maxV = 0
    for val in lst:
        if maxV < sum(val):
            maxV = sum(val)
    print(f'#{tc} {N*M-maxV}')
# ---------------------------------------------------
#     wcnt = bcnt = rcnt = 0
#     lst = []
#         for i in range(N-2):
#             for j in range(i+1, N-1):
#                 for k in range(j+1, N):
#                     if arr[i][n] != 'W':
#                         wcnt += 1
#                     if arr[j][n] != 'B':
#                         bcnt += 1
#                     if arr[k][n] != 'R':
#                         rcnt += 1
#                 lst.append([wcnt, bcnt, rcnt])
#                 wcnt = bcnt = rcnt = 0
#     print(lst)
    # minV = 9999999
    # for val in lst:
    #     if minV > sum(val):
    #         minV = sum(val)
    # print(minV)
# count 사용법

# b = 'ox o x oxoxox'
# b.count('ox')
# 4
# ---------------
# a = [1, 1, 1, 2, 3]
# a.count(1)
# 3