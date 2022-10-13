N = 7
arr = [[0] * N for _ in range(N)]

# # 상우하좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 대각선
dr2 = [-1, -1, 1, 1]
dc2 = [-1, 1, 1, -1]

r, c = 2, 2     # 기준점
arr[r][c] = '*'


# for i in range(1, 3):      # i의 시작점을 0 부터 시작하면 기준점도 바꾸고 진행
#     nr, nc = r + dr[1]*i, c + dc[1]*i
#     arr[nr][nc] = 1

# M = 3
# for dir in range(4):    # 네 방향에 대해서
#     for i in range(1, M):
#         nr, nc = r + dr[dir]*i, c + dc[dir]*i
#         if 0 <= nr < N and 0 <= nc < N:     # 이 코드가 없으면 범위를 언젠가 벗어나서 오류남
#             arr[nr][nc] = dir + 1

# ----------------------------------
nr, nc = r, c

# nr, nc = nr + dr[1], nc + dc[1]
# arr[nr][nc] = 1
#
# nr, nc = nr + dr[1], nc + dc[1]
# arr[nr][nc] = 2
#
# nr, nc = nr + dr[1], nc + dc[1]
# arr[nr][nc] = 3

for _ in range(1, N):
    nr, nc = nr + dr[1], nc + dc[1]
    if not (0 <= nr < N and 0 <= nc < N):
        break
    arr[nr][nc] = 1

while 0 <= nr + dr[1] < N and 0 <= nc + dr[1]  < N:
    nr, nc = nr +dr[1], nc + dc[1]
    arr[nr][nc] = 1



#
# for dir in range(4):
#     nr, nc = r + dr[dir], c + dc[dir]
#     if 0 <= nr < N and 0 <= nc < N:
#         arr[nr][nc] = dir + 1

for line in arr:
    print(*line)

