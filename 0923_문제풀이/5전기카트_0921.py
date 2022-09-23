import sys; sys.stdin = open('전기카트.txt')

# -------------------------------------------
# # 교수님 풀이
# N = int(input())
# G = [list(map(int, input().split())) for _ in range(N)]

# # order = [0, 1, 2, 3]
# order = [i for i in range(N)]   # 0~(n-1) 방문 순서를 저장(순열을 저장)
#
# def backtrack(k):
#     if k == N:
#         print(order + [0])
#     else:
#         for i in range(k, N):
#             order[k], order[i] = order[i], order[k]
#             backtrack(k + 1)
#             order[k], order[i] = order[i], order[k]
#
# backtrack(1)

# order = [i for i in range(N)]   # 0~(n-1) 방문 순서를 저장(순열을 저장)
#
# def backtrack(k):
#     if k == N:
#         cost = 0
#         for i in range(0, N -1):
#             # i --> i +1
#             cost += G[order[i]][order[i + 1]]
#         cost += G[order[N - 1]][0]
#         print(cost)
#     else:
#         for i in range(k, N):
#             order[k], order[i] = order[i], order[k]
#             backtrack(k + 1)
#             order[k], order[i] = order[i], order[k]
#
# backtrack(1)

# order = [i for i in range(N)]   # 0~(n-1) 방문 순서를 저장(순열을 저장)
# --------------------------------------------
# 여기부터 답은 나옴
# def backtrack(k):
#     global ans
#     if k == N:
#         cost = 0
#         for i in range(0, N -1):
#             # i --> i +1
#             cost += G[order[i]][order[i + 1]]
#         cost += G[order[N - 1]][0]
#         ans = min(ans, cost)
#     else:
#         for i in range(k, N):
#             order[k], order[i] = order[i], order[k]
#             # order[k - 1] ==> order[k]
#             backtrack(k + 1)
#             order[k], order[i] = order[i], order[k]
#
# ans = 0xfffff
# backtrack(1)
# print(ans)
#-----------------------------------------------------------

# order = [i for i in range(N)]   # 0~(n-1) 방문 순서를 저장(순열을 저장)
# def backtrack(k, cur_cost):
#     global ans
#     if k == N:
#         cur_cost += G[order[N - 1]][0]
#         ans = min(ans, cur_cost)
#     else:
#         for i in range(k, N):
#             order[k], order[i] = order[i], order[k]
#             # order[k - 1] ==> order[k]
#             backtrack(k + 1, cur_cost + G[order[k-1]][order[k]])
#             order[k], order[i] = order[i], order[k]
#
# ans = 0xfffff
# backtrack(1, 0)
# print(ans)
# ----------------------------------------
# 가지치기
# order = [i for i in range(N)]   # 0~(n-1) 방문 순서를 저장(순열을 저장)

# def backtrack(k, cur_cost):
#     global ans
#     if cur_cost >= ans: return
#     if k == N:
#         cur_cost += G[order[N - 1]][0]
#         ans = min(ans, cur_cost)
#     else:
#         for i in range(k, N):
#             order[k], order[i] = order[i], order[k]
#             # order[k - 1] ==> order[k]
#             backtrack(k + 1, cur_cost + G[order[k-1]][order[k]])
#             order[k], order[i] = order[i], order[k]
#
# ans = 0xfffff
# backtrack(1, 0)
# print(ans)

# ----------------------------------------------
# order 없이 하는 방법
for tc in range(1, int(input())+1):
    N = int(input())
    G = [list(map(int, input().split())) for _ in range(N)]

    def backtrack(k, cur_cost, used, prev):
        global ans
        if cur_cost >= ans: return
        if k == N:
            cur_cost += G[prev][0]
            ans = min(ans, cur_cost)
        else:
            for i in range(1, N):
                if used & (1 << i): continue
                backtrack(k + 1, cur_cost + G[prev][i], used|(1 << i), i)


    ans = 0xfffff
    backtrack(1, 0, 1, 0)     # 0번을 방문한 상태로 시작
    print(f'#{tc} {ans}')


