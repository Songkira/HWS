# 상우하좌
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

N = 10
arr = [[0] * N for _ in range(N)]
r = c = 4
arr[r][c] = '*'

# for i in range(4):          # 방향 결정
#     for j in range(1, N):   # 범위
#         nr = r + dr[i] * j
#         nc = c + dc[i] * j
#         if nr < 0 or nr >= N or nc < 0 or nc >= N:
#             break
#         arr[nr][nc] = i + 1

# if 0 <= nr < N and 0 <= nc < N:
# ---------------------------------
for i in range(8):          # 방향 결정
    nr = r + dr[i]
    nc = c + dc[i]
    while 0 <= nr < N and 0 <= nc < N:
        arr[nr][nc] = i + 1

        nr = nr + dr[i]
        nc = nc + dc[i]

for line in arr:
    print(*line)