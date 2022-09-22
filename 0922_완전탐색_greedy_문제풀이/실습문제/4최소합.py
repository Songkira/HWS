import sys; sys.stdin = open('최소합.txt')

# N = 7
# cnt = 0
# def dfs(r, c):
#     global cnt
#     if r == N - 1 and c == N - 1:
#         # 도착
#         cnt += 1
#     # 사실상 백트래킹?
#     else:
#         if c + 1 < N:
#             dfs(r, c + 1)
#         if r + 1 < N:
#             dfs(r + 1, c)
#
# dfs(0, 0)
# print('경로의 수=', cnt)
# # ------------------------------------------------
# arr = []
# N = 7
# cnt = 0
# ans = 0xfffffffff
# def dfs(r, c, cur_sum):
#     global cnt, ans
#     if r == N - 1 and c == N - 1:
#         ans = min(ans, cur_sum)
#         cnt += 1
#     else:
#         if c + 1 < N:
#             dfs(r, c + 1, cur_sum + arr[r][c + 1])
#         if r + 1 < N:
#             dfs(r + 1, c, cur_sum + arr[r + 1][c])
#
# dfs(0, 0, arr[0][0])
# print(ans)


# for tc in range(1, int(input())+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     ans = 0xfffffffff
#     def dfs(r, c, cur_sum):
#         global ans
#         if r == N - 1 and c == N - 1:
#             ans = min(ans, cur_sum)
#         # 사실상 백트래킹?
#         else:
#             if c + 1 < N:
#                 dfs(r, c + 1, cur_sum + arr[r][c + 1])
#             if r + 1 < N:
#                 dfs(r + 1, c, cur_sum + arr[r + 1][c])
#
#
#     dfs(0, 0, arr[0][0])
# # ---------------------------
# # return value
# # 점화식 구현
# for tc in range(1, int(input())+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     ans = 0xfffffffff
#
#     def dfs(r, c):
#         if r == 0 and c == 0:
#             return arr[0][0]
#         else:
#             left = up = 0xffffffff
#             if c - 1 >= 0:
#                 left = dfs(r, c - 1)
#             if r - 1 >= 0:
#                 up = dfs(r - 1, c)
#             return min(left, up) + arr[r][c]
#
#     print(f'#{tc}', dfs(N - 1, N - 1))

# # -----------------------------------------
# # 가지치기
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     ans = 0xfffffffff
#     memo = [[-1] * N for _ in range(N)]
#     def dfs(r, c):
#         if r == 0 and c == 0:
#             return arr[0][0]
#         if memo[r][c] != -1:
#             return memo[r][c]
#         else:
#             left = up = 0xffffffff
#             if c - 1 >= 0:
#                 left = dfs(r, c - 1)
#             if r - 1 >= 0:
#                 up = dfs(r - 1, c)
#             memo[r][c] = min(left, up) + arr[r][c]
#             return memo[r][c]
#     print(f'#{tc} {dfs(N - 1, N - 1)}')
#
# # for line in memo:
# #     print(*line)
#
# for i in range(N):
#     print(*arr[i], '|', *memo[i])

# ----------------------------
# dp
for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0xfffffffff
    memo = [[0] * N for _ in range(N)]
    memo[0][0] = arr[0][0]

    for i in range(1, N):
        memo[0][i] = memo[0][i - 1] + arr[0][i]
        memo[i][0] = memo[i - 1][0] + arr[i][0]

    for i in range(1, N):
        for j in range(1, N):
            memo[i][j] = min(memo[i][j - 1], memo[i - 1][j]) + arr[i][j]

    print(f'#{tc} {memo[N - 1][N - 1]}')
