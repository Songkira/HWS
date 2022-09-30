N = 4
arr = [i for i in range(N)]

# 2그룹으로 나누고 싶다 / 부분집합 활용
# 1
def backtrack(k):
    if k == N:
        if len(A) == N //2:
            print(A, list(set(arr) - set(A)))
    else:
        A.append(arr[k])
        backtrack(k + 1)
        A.pop()

        backtrack(k + 1)
A = []
# [0, 1] [2, 3]
# [0, 2] [1, 3]
# [0, 3] [1, 2]
# [1, 2] [0, 3]
# [1, 3] [0, 2]
# [2, 3] [0, 1]

# ----------------------------------------
# 2
# def backtrack(k):
#     if k == N:
#         if len(A) == N // 2:
#             print(A, B)
#     else:
#         A.append(arr[k])
#         backtrack(k + 1)
#         A.pop()
#         B.append(arr[k])
#         backtrack(k + 1)
#         B.pop()
#
# A, B = [], []

# [0, 1] [2, 3]
# [0, 2] [1, 3]
# [0, 3] [1, 2]
# [1, 2] [0, 3]
# [1, 3] [0, 2]
# [2, 3] [0, 1]
# ---------------------------------------
# def backtrack(k):
#     if k == N:
#         if len(A) == N // 2:
#             print(A, list(set(arr) - set(A)))
#     else:
#         A.append(arr[k])
#         backtrack(k + 1)
#         A.pop()
#         backtrack(k + 1)
#
# A = [arr[0]]
#
# backtrack(1)
# [0, 1] [2, 3]
# [0, 2] [1, 3]
# [0, 3] [1, 2]

# -----------------------------------
def backtrack(k):
    if len(A) == N // 2:
        print(A, B + arr[k:])
        return
    if len(B) == N // 2:
        print(A + arr[k:], B)
        return

    A.append(arr[k])
    backtrack(k + 1)
    A.pop()

    B.append(arr[k])
    backtrack(k + 1)
    B.pop()

A, B = [arr[0]], []

backtrack(1)
# [0, 1] [2, 3]
# [0, 2] [1, 3]
# [0, 3] [1, 2]
