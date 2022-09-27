#
# def nQueen(row, visit):
#     if row == N:
#         global ans; ans += 1
#     else:
#         for col in range(N):    # 이번 col 을 열값으로 선택
#             if visit & (1 << col): continue  # 같은행, 같은 열은 제외
#             a = row + col
#             b = row - col + (N - 1)
#
#             if line1[a] or line2[b]: continue # 대각에 대해서 체크
#
#             line1[a] = line2[b] = 1
#             nQueen(row + 1, visit | (1 << col))
#             line1[a] = line2[b] = 0
#
# for i in range(1, 11):
#     N = i
#     ans = 0
#     line1 = [0] * (N + N) # 대각선 / 모양 row + col
#     line2 = [0] * (N + N) # 대각선 \ 모양 row - col + (N - 1)
#     nQueen(0, 0)
#     print(ans)

# ================================================================

def nQueen(row):
    if row == N:
        global ans;
        ans += 1
    else:
        for col in range(N):  # 이번 col 을 열값으로 선택
            if visit[col]: continue  # 같은행, 같은 열은 제외
            a = row + col
            b = row - col + (N - 1)

            if line1[a] or line2[b]: continue  # 대각에 대해서 체크

            visit[col] = line1[a] = line2[b] = 1
            nQueen(row + 1)
            visit[col] = line1[a] = line2[b] = 0


for i in range(1, 11):
    N = i
    ans = 0
    visit = [0] * N
    line1 = [0] * (N + N)  # 대각선 / 모양 row + col
    line2 = [0] * (N + N)  # 대각선 \ 모양 row - col + (N - 1)
    nQueen(0)
    print(ans)