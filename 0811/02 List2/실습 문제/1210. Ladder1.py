import sys; sys.stdin = open('1210.txt', 'r')

# T = int(input())
#
# for tc in range(T):
#     square = [list(map(int, input().split())) for _ in range(100)]
#     r = c = 0
#
#     # 하좌우
#     dr = [1, 0, 0]
#     dc = [0, -1, 1]
#     loc = 0
#     for i in range(100):
#         if square[r][c] == 1:
#             r = r + dr[loc]
#             c = c + dc[loc]
#             if square[r][c+1] == 1:  # 왼쪽
#                 loc += 1
#                 r = r + dr[loc]
#                 c = c + dr[loc]
#             elif square[r][c-1] == 1: # 오른쪽
#                 loc += 2
#                 r = r + dr[loc]
#                 c = c + dr[loc]
#
#         if square[r][c] == 2:
#             print(i)
#
# -----------------------------------------
# # T = int(input())
#
# for tc in range(1, 11):
#     tc_num = input()
#     ladder = [list(map(int, input().split())) for _ in range(100)]
#     # 도착점 ==> 출발점
#     r = c = 0
#
#     for i in range(100): # 99번(마지막)을 조사
#         if ladder[99][i] == 2:
#             r, c = 99, i
#             break
#
#     while r != 0:
#     # 반복해서 한 칸 씩 이동
#     # 내가 지나온 길은 풀 한포기도 남기지 않겠다...
#     # 복구 안하면 되돌아가기 어렵기때문에 해결책 필요.
#         ladder[r][c] = 0
#         # 왼쪽에 길이 있다면 좌로 이동
#         if c > 0 and ladder[r][c - 1]: # 인덱스 범위 벗어나는거 주의
#         # if c >= 1
#             c -= 1
#         # 왼쪽에 길이 있다면 우로 이동
#         elif c + 1 < 100 and ladder[r][c+1]:
#             c += 1
#         # 왼쪽에 길이 있다면 위로 이동
#         else:
#             r -= 1
#     print(c)
#---------------------------------------------------------------
# 왼쪽이나 오른쪽 길이 없으면 -> 위로이동
# 오른쪽길 나오면 -> 오른쪽길 없어질때까지 계속 이동한 후 위로 한칸 이동
# 왼쪽길이 나오면 -> 왼쪽길 없을때까지 계속 이동한 후 위로 한칸 이동

for tc in range(1, 11):
    tc_num = input()
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 도착점 ==> 출발점
    r = c = 0

    for i in range(100): # 99번(마지막)을 조사
        if ladder[99][i] == 2:
            r, c = 99, i
            break

    while r: #  반복해서 한칸씩 이동
        if c > 0 and ladder[r][c - 1]: # 길이 있다면 좌로이동
            while c > 0 and ladder[r][c - 1]:
                c -= 1
        elif c < 99 and ladder[r][c + 1]: # 길이 있따면 우로 이동
            while c < 99 and ladder[r][c + 1]:
               c += 1
        # 위로 이동
        r -= 1
