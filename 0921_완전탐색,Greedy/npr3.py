# # 재귀 호출을 통한 순열 생성2
# def f(i, k):
#     if i == k:
#         print(p)
#     else:
#         for j in range(k):
#             if used[j] == 0:        # a[j]가 아직 사용되지 않았으면
#                 used[j] = 1         # a[j] 사용됨으로 표시
#                 p[i] = a[j]         # p[i]는 a[j]로 결정
#                 f(i+1, k)           # p[i+1] 값을 결정하러 이동
#                 used[j] = 0         # a[j]를 다른 자리에서 쓸 수 있도록 해제

# N = 3
# a = [i for i in range(1, N+1)]
# used = [0] * N
# p = [0] * N
# f(0, N)

# --------------------------
# N개 중에 R개 구하는 경우
def f(i, k, r):
    if i == r:
        print(p)
    else:
        for j in range(k):
            if used[j] == 0:        # a[j]가 아직 사용되지 않았으면
                used[j] = 1         # a[j] 사용됨으로 표시
                p[i] = a[j]         # p[i]는 a[j]로 결정
                f(i+1, k, r)           # p[i+1] 값을 결정하러 이동
                used[j] = 0

# # 연습문제 2 활용
# N = 6  # 주어진 개수
# R = 6   # 고르는 개수
# # a = [i for i in range(1, N+1)]
# a = [1, 2, 4, 7, 8, 3]
# used = [0] * N
# p = [0] * R
# f(0, N, R)

# -------------------------
# 1은 고정으로 두고 나머지만 만들어보는 경우
# N = 5  # 주어진 개수
# R = 5   # 고르는 개수
# a = [i for i in range(1, N+1)]
# # a = [1, 2, 4, 7, 8, 3]
# used = [0] * N
# p = [0] * R
# p[0] = 1
# used[0] = 1
# f(1, N, R)

# ------------------------------
# 앞자리 2를 고정으로 두고 나머지만 만들어보는 경우
N = 5  # 주어진 개수
R = 5   # 고르는 개수
a = [i for i in range(1, N+1)]
# a = [1, 2, 4, 7, 8, 3]
used = [0] * N
p = [0] * R
p[0] = 2
used[1] = 1
f(1, N, R)
