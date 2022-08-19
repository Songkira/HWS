import sys; sys.stdin = open('스도쿠.txt', 'r')

# def sort_lst(n):
#     for i in range(1, 9-1):
#         min_idx = i
#         for j in range(i+1, 9):
#             if n[min_idx] > n[j]:
#                 min_idx = j
#         n[i], n[min_idx] = n[min_idx], n[i]

for tc in range(1, int(input())+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = 1

    num = 0
    for i in range(9):
        ver = []
        row = []
        for j in range(9):
            if arr[i][j] not in row:
                row.append(arr[i][j])
            else:
                result = 0
                break
            if arr[j][i] not in ver:
                ver.append(arr[j][i])
            else:
                result = 0
                break

    for i in range(0,9-3+1,3):
        for j in range(0, 9-3+1, 3):
            square = []
            for r in range(3):
                for c in range(3):
                    if arr[r+i][c+j] not in square:
                        square.append(arr[r+i][c+j])
                    else:
                        result = 0
                        break
    print(f'#{tc} {result}')
#----------------------------------------------------
# for case in range(1, int(input()) + 1):
#     # 스도쿠
#     sdoku = [list(map(int, input().split())) for _ in range(9)]
#
#
#     # 행과 열이 모두 1~9로(중복 없이) 채워졌는지 확인
#     def sdukuOvl():
#         # 결과값 1로 최기화
#         result = 1
#         for r in range(9):
#             # 인덱스를 활용할 배열 초기화
#             rowCnt = [0] * 11
#             colCnt = [0] * 11
#
#             for c in range(9):
#                 rowCnt[sdoku[r][c]] += 1
#                 colCnt[sdoku[c][r]] += 1
#             # print(sdoku[c][r])
#             # 1~9까지 없거나 한 번 이상 나오면 0
#             for i in range(1, 10):
#                 if rowCnt[i] != 1 or colCnt[i] != 1:
#                     result = 0
#                     return result
#
#         # 사각형에 모두 1~9로 (중복 없이) 채워졌는지 확인
#         for r in range(0, 7, 3):
#             for c in range(0, 7, 3):
#                 # 인덱스를 활용할 배열 초기화
#                 square = [0] * 11
#
#                 for nr in range(r, r + 3):
#                     for nc in range(c, c + 3):
#                         square[sdoku[nr][nc]] += 1
#                 # 1~9까지 없거나 한 번 이상 나오면 0
#                 for i in range(1, 10):
#                     if square[i] != 1:
#                         result = 0
#                         return result
#         return result


    result = sdukuOvl()

    print(f'#{case} {result}')