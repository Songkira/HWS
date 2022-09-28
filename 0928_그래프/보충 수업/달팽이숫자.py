
N = 5
arr = [[0] * N for _ in range(N)]

dr = [0, 1, 0, -1] # 우(0)하(1)좌(2)상(3)우(0)...
dc = [1, 0, -1, 0] # 방향전환 dir = (dir + 1) % 4

r, c = 0, -1

# while True:
#     r, c = r + dr[0], c + dc[0]
#     if 0 <= r < N and 0 <= c < N:
#         arr[r][c] = 1
#     else:
#         r, c = r - dr[0], c - dc[0]
#         break
#
# while True:
#     r, c = r + dr[1], c + dc[1]
#     if 0 <= r < N and 0 <= c < N:
#         arr[r][c] = 2
#     else:
#         r, c = r - dr[1], c - dc[1]
#         break
# ---------------------------------

# dir = 0
# while dir < 4:
#     r, c = r + dr[dir], c + dc[dir]
#     if 0 <= r < N and 0 <= c < N:
#         arr[r][c] = dir + 1
#     else:
#         r, c = r - dr[dir], c - dc[dir]
#         dir = dir + 1
# -----------------------------------------

# dir = 0
# while dir < 4:
#     r, c = r + dr[dir], c + dc[dir]
#     if 0 <= r < N and 0 <= c < N and arr[r][c] == 0:
#         arr[r][c] = dir + 1
#     else:
#         r, c = r - dr[dir], c - dc[dir]
#         dir = dir + 1
# -------------------------------------------
num = 1
dir = 0
while num <= N * N:
    r, c = r + dr[dir], c + dc[dir]
    if 0 <= r < N and 0 <= c < N and arr[r][c] == 0:
        arr[r][c] = num
        num += 1
    else:
        r, c = r - dr[dir], c - dc[dir]
        dir = (dir + 1) % 4


# for i in range(1, N*N+1):


for line in arr:
    print(*line)