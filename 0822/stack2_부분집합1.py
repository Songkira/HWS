# 부분집합 전부를 생성하는 경우
# def f(i, N):
#     if i == N:
#         print(bit)
#     else:
#         bit[i] = 1 # A[i]가 부분집합에 포함
#         f(i+1, N)
#         bit[i] = 0
#         f(i+1, N)
#
# A = [1, 2, 3]
# bit = [0] * 3
# f(0, 3)
# [1, 1, 1]
# [1, 1, 0]
# [1, 0, 1]
# [1, 0, 0]
# [0, 1, 1]
# [0, 1, 0]
# [0, 0, 1]
# [0, 0, 0]
# 비트로 구성된 부분집합 배열 나타내기
# def f(i, N):
#     if i == N:
#         print(bit)
#     else:
#         bit[i] = 1 # A[i]가 부분집합에 포함
#         f(i+1, N)
#         bit[i] = 0
#         f(i+1, N)
#
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# bit = [0] * 10
# f(0, 10)

# --------------------------
# 실제 부분집합 배열 나타내기
# def f(i, N):
#     if i == N:
#         for i in range(N):
#             if bit[i]:
#                 print(A[i], end=' ')
#         print()
#     else:
#         bit[i] = 1 # A[i]가 부분집합에 포함
#         f(i+1, N)
#         bit[i] = 0
#         f(i+1, N)
#
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# bit = [0] * 10
# f(0, 10)
# ------------------------
# 합
# def f(i, N):
#     global answer
#     if i == N:
#         s = 0                       # 부분집합의 합
#         for i in range(N):
#             if bit[i]:
#                 s += A[i]
#                 # print(A[i], end=' ')
#         # print()
#         if s == 10:
#             answer += 1 # 부분집합의 합이 10인 경우의 수
#     else:
#         bit[i] = 1 # A[i]가 부분집합에 포함
#         f(i+1, N)
#         bit[i] = 0
#         f(i+1, N)
#
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# bit = [0] * 10
# answer = 0
# f(0, 10)
# print(answer) # 10
# --------------------------------
# def f(i, N):
#     global answer
#     if i == N:
#         s = 0
#         for i in range(N):
#             if bit[i]:
#                 s += A[i]
#         if s == 10:
#             answer += 1 # 부분집합의 합이 10인 경우의 수
#             for i in range(N):
#                 if bit[i]:
#                     print(A[i], end = ' ')
#             print()
#     else:
#         bit[i] = 1 # A[i]가 부분집합에 포함
#         f(i+1, N)
#         bit[i] = 0
#         f(i+1, N)
#
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# bit = [0] * 10
# answer = 0
# f(0, 10)
# print(answer)
# 1 2 3 4
# 1 2 7
# 1 3 6
# 1 4 5
# 1 9
# 2 3 5
# 2 8
# 3 7
# 4 6
# 10
# 10
# --------------------------------------
def f(i, N):
    global answer
    global cnt
    cnt += 1
    if i == N:
        s = 0
        for i in range(N):
            if bit[i]:
                s += A[i]
        if s == 10:
            answer += 1 # 부분집합의 합이 10인 경우의 수
            for i in range(N):
                if bit[i]:
                    print(A[i], end = ' ')
            print()
    else:
        bit[i] = 1 # A[i]가 부분집합에 포함
        f(i+1, N)
        bit[i] = 0
        f(i+1, N)

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * 10
answer = 0
cnt = 0
f(0, 10)
print(answer, cnt)
