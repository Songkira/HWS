N = 10
# 0 은 정수는 immutable 타입이라 괜찮음.
arr = [[0] * N for _ in range(N)]

# r = c =5
# arr[r][c] = '*'
# arr[r - 1][c + 0] = 1 # 위
# arr[r + 1][c + 0] = 2 # 아래
# arr[r + 0][c - 1] = 3 # 좌
# arr[r + 0][c + 1] = 4 # 우
# delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# =======================
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]

# for i in range(4):
#     nr = r + dr[i]
#     nc = c + dc[i]
#     arr[nr][nc] = i + 1
# ====================
# r = c = 5
# arr[r][c] = '*'
# # 위로
# for i in range(r -1 , -1, -1):
#     arr[i][c] = 1
# # 아래로
# for i in range(r + 1 , N):
#     arr[i][c] = 2
# # 왼쪽
# for i in range(c -1 , -1, -1):
#     arr[r][i] = 3
# # 오른쪽
# for i in range(c + 1 ,N):
#     arr[r][i] = 4
# ================================
# 델타
r = c = 5
arr[r][c] = '*'

# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
# for i in range(4):# 방향을 선택
#     for j in range(1, N):
#         nr, nc = r + dr[i] * j, c + dc[i] * j
#         if nr < 0 or nr >= N or nc < 0 or nc >= N:
#             break
#         arr[nr][nc] = i + 1
# ====================================
# 대각선 방향
dr = [-1, -1, 1, 1]
dc = [-1, 1, 1, -1]
for i in range(4):# 방향을 선택
    for j in range(1, N):
        nr, nc = r + dr[i] * j, c + dc[i] * j
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            break
        arr[nr][nc] = i + 1

for line in arr:
    print(*line) # * -> 언팩 : 리스트 벗기는거