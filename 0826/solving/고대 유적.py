import sys; sys.stdin = open('고대 유적.txt', 'r')

for tc in range(1, int(input())+1):
    # N = 줄의 갯수, M = 데이터의 개수(열의 개수 인가?)
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max = 0
    row = [0]
    ver = [0]
    for i in range(N):
        row_cnt = 0
        for j in range(M):
            if arr[i][j] == 1:
                row_cnt += 1
                if row_cnt == M:
                    row.append(row_cnt)
                if j == M-1:
                    row.append(row_cnt)
            else:
                if row_cnt == 0:
                    pass
                else:
                    row.append(row_cnt)
                row_cnt = 0

    for i in range(M):
        ver_cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                ver_cnt += 1
                if ver_cnt == N:
                    ver.append(ver_cnt)
                if i == N-1:
                    ver.append(ver_cnt)
            else:
                if ver_cnt == 0:
                    pass
                else:
                    ver.append(ver_cnt)
                ver_cnt = 0

    ver.sort()
    row.sort()
    # for i in range(len(ver)-1):
    #     min_idx = i
    #     for j in range(i+1, len(ver)):
    #         if ver[min_idx] > ver[j]:
    #             min_idx = j
    #             ver[i], ver[min_idx] = ver[min_idx], ver[i]
    #
    # for i in range(len(row)-1):
    #     min_idx = i
    #     for j in range(i+1, len(row)):
    #         if row[min_idx] > row[j]:
    #             min_idx = j
    #             row[i], row[min_idx] = row[min_idx], row[i]

    # print(ver)
    # print(row)
    if ver[-1] >= row[-1]:
        print(f'#{tc} {ver[-1]}')
    else:
        print(f'#{tc} {row[-1]}')

    # print(max)